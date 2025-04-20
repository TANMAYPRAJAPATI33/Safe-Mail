import re
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

def extract_features(email_text):
    if not isinstance(email_text, str):
        return {
            'email_length': 0,
            'word_count': 0,
            'url_count': 0,
            'special_char_count': 0,
            'suspicious_keywords_count': 0,
            'exclamation_count': 0,
            'dollar_count': 0,
            'all_caps_words_count': 0,
            'click_here_count': 0,
            'free_count': 0,
            'urgent_count': 0,
            'money_count': 0,
            'prize_count': 0,
            'congratulations_count': 0,
            'winner_count': 0,
            'offer_count': 0,
            'limited_time_count': 0
        }

    features = {}

    email_lower = email_text.lower()
    words = email_text.split()

    features['email_length'] = len(email_text)
    features['word_count'] = len(words)
    features['url_count'] = len(re.findall(r'https?://\S+|www\.\S+', email_lower))
    features['special_char_count'] = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', email_text))
    features['exclamation_count'] = email_text.count('!')
    features['dollar_count'] = email_text.count('$')
    features['all_caps_words_count'] = sum(1 for word in words if word.isupper() and len(word) > 2)

    features['click_here_count'] = email_lower.count('click here')
    features['free_count'] = email_lower.count('free')
    features['urgent_count'] = email_lower.count('urgent')
    features['money_count'] = email_lower.count('money')
    features['prize_count'] = email_lower.count('prize')
    features['congratulations_count'] = email_lower.count('congratulations')
    features['winner_count'] = email_lower.count('winner') + email_lower.count('won')
    features['offer_count'] = email_lower.count('offer')
    features['limited_time_count'] = email_lower.count('limited time')

    suspicious_keywords = ['free', 'offer', 'win', 'urgent', 'money', 'prize', 'click', 
                           'congratulations', 'winner', 'won', 'limited', 'act now', 
                           'exclusive', 'guaranteed', 'cash', 'credit', 'investment',
                           'opportunity', 'discount', 'save', 'alert', 'important']

    features['suspicious_keywords_count'] = sum(email_lower.count(word) for word in suspicious_keywords)

    return features

class FeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if isinstance(X, np.ndarray):
            emails = X.flatten().tolist()
        elif isinstance(X, list):
            emails = X
        else:
            raise TypeError(f"Expected input type to be list or ndarray, but got {type(X)}")

        feature_dicts = [extract_features(email) for email in emails]
        feature_array = np.array([[v for v in feat.values()] for feat in feature_dicts])

        return feature_array
