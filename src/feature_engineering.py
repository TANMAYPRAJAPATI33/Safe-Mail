# feature_engineering.py

import re

def extract_features(email_text):
    """
    Extract engineered features from email text.
    
    Args:
        email_text (str): The raw email text.
    
    Returns:
        dict: A dictionary with extracted features.
    """
    # Ensure the input is a string; if not, return default feature values.
    if not isinstance(email_text, str):
        return {
            'email_length': 0,
            'word_count': 0,
            'url_count': 0,
            'special_char_count': 0,
            'suspicious_keywords_count': 0
        }
    
    features = {}
    
    # Email length (number of characters)
    features['email_length'] = len(email_text)
    
    # Word count
    features['word_count'] = len(email_text.split())
    
    # Count URLs using a regex pattern
    features['url_count'] = len(re.findall(r'https?://\S+', email_text))
    
    # Count special characters (you can customize this regex as needed)
    features['special_char_count'] = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', email_text))
    
    # Count suspicious keywords
    suspicious_keywords = ['free', 'offer', 'win', 'urgent', 'money', 'prize', 'click']
    features['suspicious_keywords_count'] = sum(email_text.lower().count(word) for word in suspicious_keywords)
    
    return features

if __name__ == '__main__':
    # Quick test on a sample email
    sample_email = """
    <html><body>Congratulations! You've WON a free prize. Click <a href="https://example.com">here</a> to claim your prize!</body></html>
    """
    print("Extracted Features:")
    features = extract_features(sample_email)
    for key, value in features.items():
        print(f"{key}: {value}")
