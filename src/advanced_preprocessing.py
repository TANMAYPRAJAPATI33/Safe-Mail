import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def preprocess(email_text):
   
    if not isinstance(email_text, str):
        return ""
    
    email_text = email_text.lower()
    email_text = re.sub(r'<[^>]+>', ' ', email_text)
    email_text = re.sub(r'[^a-z\s]', '', email_text)
    
    tokens = word_tokenize(email_text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return " ".join(tokens)

if __name__ == '__main__':
    sample_email = """
    <html><body>Congratulations! You've WON a free prize. Click <a href="https://example.com">here</a> to claim your prize!</body></html>
    """
    print("Original Email:")
    print(sample_email)
    print("\nPreprocessed Email:")
    print(preprocess(sample_email))
