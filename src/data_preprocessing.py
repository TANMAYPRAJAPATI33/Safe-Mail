import pandas as pd
from sklearn.model_selection import train_test_split
import re
import nltk
from nltk.corpus import stopwords

print("Data preprocessing script started")  

def basic_cleaning(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


nltk.download('stopwords', quiet=True)
raw_stop_words = stopwords.words('english')

clean_stop_words = list(set(basic_cleaning(word) for word in raw_stop_words))

def load_data(filepath):
    print(f"Loading data from {filepath}")  
    df = pd.read_csv(filepath)
    print(f"Data loaded, shape: {df.shape}")  
    return df

def split_data(df, test_size=0.5, random_state=42):
    X = df['text']
    y = df['label']
    print("Splitting data...")  
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )
    print("Data split complete")  
    return X_train, X_test, y_train, y_test

def get_vectorizer():
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(
        preprocessor=basic_cleaning,
        stop_words=clean_stop_words,  
        max_features=3000
    )
    return vectorizer

if __name__ == "__main__":
    df = load_data("data/spam_dataset.csv")
    X_train, X_test, y_train, y_test = split_data(df)
    print("Training set size:", len(X_train))
    print("Test set size:", len(X_test))
    
    sample_text = "Hello there! <b>Win $100</b> now!!!"
    print("Original:", sample_text)
    print("Cleaned:", basic_cleaning(sample_text))
    
    texts = ["Hello, win money now!", "Hi, how are you doing?"]
    vectorizer = get_vectorizer()
    features = vectorizer.fit_transform(texts)
    print("Feature shape:", features.shape)
