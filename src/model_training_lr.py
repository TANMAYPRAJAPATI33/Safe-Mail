import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from data_preprocessing import load_data, split_data, get_vectorizer

def train_logistic_regression_model(data_path, model_output_path, test_size=0.5, random_state=42):
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = split_data(df, test_size=test_size, random_state=random_state)
    
    vectorizer = get_vectorizer()
    
    lr_pipeline = Pipeline([
        ('tfidf', vectorizer),
        ('clf', LogisticRegression(solver='liblinear'))
    ])
    
    lr_pipeline.fit(X_train, y_train)
    
    joblib.dump(lr_pipeline, model_output_path)
    print("Logistic Regression model trained and saved to", model_output_path)
    
    return lr_pipeline, X_test, y_test

if __name__ == "__main__":
    train_logistic_regression_model("data/spam_dataset.csv", "models/logistic_regression_model.pkl")
