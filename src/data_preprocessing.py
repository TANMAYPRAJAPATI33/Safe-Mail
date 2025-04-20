import pandas as pd
from sklearn.model_selection import train_test_split
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

print("Data preprocessing script started")

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt', quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def advanced_cleaning(text):
    """Enhanced text cleaning for email content"""
    if not isinstance(text, str):
        return ""
    

    text = text.lower()
    
    
    text = re.sub(r'<.*?>', '', text)
    
   
    text = re.sub(r'http\S+|www\S+', '', text)
    
   
    text = re.sub(r'\S+@\S+', '', text)
    

    text = re.sub(r'[^\w\s]', '', text)
    

    text = re.sub(r'\d+', '', text)
    
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def extract_features(text):
    """Extract additional features for spam detection"""
    features = {}
    
   
    features['exclamation_count'] = text.count('!')
    
    
    features['dollar_count'] = text.count('$')
    
    
    features['all_caps_count'] = len(re.findall(r'\b[A-Z]{2,}\b', text))
    
  
    features['url_count'] = len(re.findall(r'http\S+|www\S+', text))
    

    suspicious_phrases = ['free', 'win', 'winner', 'cash', 'prize', 'money', 'offer', 'credit', 'loan', 'limited time']
    features['suspicious_phrase_count'] = sum(1 for phrase in suspicious_phrases if phrase in text.lower())
    
    return features

def load_data(filepath):
    print(f"Loading data from {filepath}")
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded, shape: {df.shape}")
        
        
        print(f"Checking for missing values...")
        print(f"NaN values in text column: {df['text'].isna().sum()}")
        
       
        df = df.dropna(subset=['text'])
        print(f"Rows after dropping NaN values: {len(df)}")
        
        df['text'] = df['text'].astype(str)
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame(columns=['text', 'label'])

def split_data(df, test_size=0.2, random_state=42):
    X = df['text']
    y = df['label']
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    
    X_train = X_train.astype(str)
    X_test = X_test.astype(str)
    
    print("Data split complete")
    return X_train, X_test, y_train, y_test

def get_vectorizer():
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(
        preprocessor=advanced_cleaning,
        stop_words='english',
        max_features=5000,
        ngram_range=(1, 2),
        min_df=3, 
        max_df=0.9 
    )
    return vectorizer

if __name__ == "__main__":
    df = load_data("data/expanded_spam_dataset.csv")
    X_train, X_test, y_train, y_test = split_data(df)
    print("Training set size:", len(X_train))
    print("Test set size:", len(X_test))
    
    sample_text = "Hello there! <b>Win $100</b> now!!!"
    print("Original:", sample_text)
    print("Cleaned:", advanced_cleaning(sample_text))