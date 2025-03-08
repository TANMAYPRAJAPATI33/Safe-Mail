import os
import pandas as pd

def load_emails_from_dir(root_dir, label):
    """
    Recursively load all email files from a directory and label them.
    """
    emails = []
    for current_root, dirs, files in os.walk(root_dir):
        for filename in files:
            file_path = os.path.join(current_root, filename)
            try:
                with open(file_path, 'r', encoding='latin-1') as f:
                    text = f.read()
                    emails.append((text, label))
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return emails

spam_path = 'data/spamassassin/spam'
ham_path = 'data/spamassassin/ham'

print("Loading spam emails...")
spam_emails = load_emails_from_dir(spam_path, 'spam')
print(f"Loaded {len(spam_emails)} spam emails.")

print("Loading ham emails...")
ham_emails = load_emails_from_dir(ham_path, 'ham')
print(f"Loaded {len(ham_emails)} ham emails.")

all_emails = spam_emails + ham_emails

df = pd.DataFrame(all_emails, columns=['text', 'label'])

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

output_csv = 'data/expanded_spam_dataset.csv'
df.to_csv(output_csv, index=False)
print(f"Dataset saved to {output_csv}. Total samples: {len(df)}")

