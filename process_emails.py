import imaplib
import email
from email.header import decode_header
import joblib
import sys
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
IMAP_SERVER = "imap.gmail.com" 
MODEL_PATH = "models/spam_detector.pkl"

MOVE_THRESHOLD = 0.90   
DELETE_THRESHOLD = 0.80 

def connect_email():
    """Connect to the email inbox using IMAP with an app password."""
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")
        return mail
    except Exception as e:
        print("Error connecting to email:", e)
        sys.exit(1)
def fetch_unread_emails(mail):
    """Fetch unread emails from the inbox."""
    try:
        status, messages = mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()
        emails = []
        for num in email_ids:
            status, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")
            sender = msg.get("From")
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" not in content_disposition:
                        try:
                            body = part.get_payload(decode=True).decode()
                        except Exception:
                            pass
            else:
                try:
                    body = msg.get_payload(decode=True).decode()
                except Exception:
                    pass
            emails.append({"id": num, "subject": subject, "sender": sender, "body": body})
        return emails
    except Exception as e:
        print("Error fetching emails:", e)
        return []

def move_to_spam(mail, email_id):
    """Move an email to the Spam folder."""
    try:
        mail.store(email_id, "+FLAGS", "\\Seen")
        mail.copy(email_id, "Spam")
        mail.store(email_id, "+FLAGS", "\\Deleted")
        mail.expunge()
        return "Moved to Spam folder"
    except Exception as e:
        return f"Error moving email: {e}"

def delete_email(mail, email_id):
    """Delete an email from the inbox."""
    try:
        mail.store(email_id, "+FLAGS", "\\Deleted")
        mail.expunge()
        return "Deleted from Inbox"
    except Exception as e:
        return f"Error deleting email: {e}"

def process_emails():
    """Load model, process unread emails, and take appropriate action with clear output."""
    print("Data preprocessing script started\n")
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        print("Error: Model file is missing in the models/ directory.")
        sys.exit(1)
    except Exception as e:
        print("Error loading model:", e)
        sys.exit(1)
    
    mail = connect_email()
    emails = fetch_unread_emails(mail)
    
    if not emails:
        print("No unread emails found.")
        mail.logout()
        return

    for email_data in emails:
        raw_text = email_data["body"] or ""
        email_id = email_data["id"]
        subject = email_data["subject"]

        
        if not isinstance(raw_text, str):
            print(f"Skipping email {email_id} because its body is not a string.\n")
            continue

       
        processed_text = raw_text.lower()
        
        try:
            
            prediction = model.predict([processed_text])[0]
            probabilities = model.predict_proba([processed_text])[0]
            spam_index = list(model.classes_).index("spam") if "spam" in model.classes_ else 1
            spam_prob = probabilities[spam_index]
        except Exception as e:
            print(f"Error during prediction for email {email_id}: {e}\n")
            continue

        
        spam_prob_pct = spam_prob * 100
        
       
        if prediction == "spam":
            if spam_prob >= MOVE_THRESHOLD:
                action = move_to_spam(mail, email_id)
            elif spam_prob >= DELETE_THRESHOLD:
                action = delete_email(mail, email_id)
            else:
                action = "No action taken due to low confidence"
        else:
            action = "Email is not spam"
        print("-" * 50)
        print(f"Email ID   : {email_id.decode() if isinstance(email_id, bytes) else email_id}")
        print(f"Subject    : {subject}")
        print(f"Prediction : {prediction}")
        print(f"Spam Prob. : {spam_prob_pct:.2f}%")
        print(f"Action     : {action}")
        print("-" * 50 + "\n")
    
    mail.logout()

if __name__ == "__main__":
    process_emails()
