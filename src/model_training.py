import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from data_preprocessing import load_data, split_data, get_vectorizer

def train_naive_bayes_model(data_path, model_output_path, test_size=0.5, random_state=42):
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = split_data(df, test_size=test_size, random_state=random_state)
    
    vectorizer = get_vectorizer()
    
    nb_pipeline = Pipeline([
        ('tfidf', vectorizer),
        ('clf', MultinomialNB())
    ])
    
    nb_pipeline.fit(X_train, y_train)
    
    joblib.dump(nb_pipeline, model_output_path)
    
    print("Model trained and saved to", model_output_path)
    return nb_pipeline, X_test, y_test

if __name__ == "__main__":
    model, X_test, y_test = train_naive_bayes_model("data/expanded_spam_dataset.csvv", "models/naive_bayes_model.pkl")
