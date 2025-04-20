#!/usr/bin/env python3
import os
import csv
import email
import re
from email.parser import Parser

def extract_email_features(file_path):
    """Extract relevant features from an email file."""
    
    # Read the email file
    with open(file_path, 'r', encoding='latin-1') as file:
        content = file.read()
    
    # Parse the email
    email_parser = Parser()
    msg = email_parser.parsestr(content)
    
    # Extract basic headers
    subject = msg.get('Subject', '')
    from_address = msg.get('From', '')
    to_address = msg.get('To', '')
    date = msg.get('Date', '')
    
    # Get email body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                try:
                    body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
                except:
                    body += str(part.get_payload())
    else:
        try:
            body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        except:
            body = str(msg.get_payload())
    
    # Clean up body text
    body = re.sub(r'\s+', ' ', body).strip()
    
    return {
        'subject': subject,
        'from': from_address,
        'to': to_address,
        'date': date,
        'body': body
    }

def convert_spamassassin_to_csv(spam_dir, ham_dir, output_file):
    """Convert SpamAssassin dataset to CSV format."""
    
    # Print debug information
    print("Starting conversion process...")
    print("Current working directory:", os.getcwd())
    print(f"Spam directory path: {spam_dir}")
    print(f"Ham directory path: {ham_dir}")
    print(f"Spam directory exists: {os.path.exists(spam_dir)}")
    print(f"Ham directory exists: {os.path.exists(ham_dir)}")
    
    fieldnames = ['label', 'subject', 'from', 'to', 'date', 'body']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Process spam emails
        print(f"Processing spam emails from {spam_dir}...")
        spam_count = 0
        for file_name in os.listdir(spam_dir):
            file_path = os.path.join(spam_dir, file_name)
            if os.path.isfile(file_path):
                try:
                    email_data = extract_email_features(file_path)
                    email_data['label'] = 'spam'
                    writer.writerow(email_data)
                    spam_count += 1
                    if spam_count % 100 == 0:
                        print(f"Processed {spam_count} spam emails")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
        
        # Process ham emails
        print(f"Processing ham emails from {ham_dir}...")
        ham_count = 0
        for file_name in os.listdir(ham_dir):
            file_path = os.path.join(ham_dir, file_name)
            if os.path.isfile(file_path):
                try:
                    email_data = extract_email_features(file_path)
                    email_data['label'] = 'ham'
                    writer.writerow(email_data)
                    ham_count += 1
                    if ham_count % 100 == 0:
                        print(f"Processed {ham_count} ham emails")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    print(f"Conversion complete. Processed {spam_count} spam and {ham_count} ham emails.")
    print(f"Output saved to {output_file}")

# Main execution block
if __name__ == "__main__":
    # Get current directory (where the script is running)
    current_dir = os.getcwd()
    
    # Set paths relative to current directory
    spam_dir = os.path.join(current_dir, 'spam')
    ham_dir = os.path.join(current_dir, 'ham')
    output_file = os.path.join(current_dir, 'spamassassin_converted.csv')
    
    print(f"Will save output to: {output_file}")
    convert_spamassassin_to_csv(spam_dir, ham_dir, output_file)
