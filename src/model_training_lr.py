# src/model_training_lr.py

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from data_preprocessing import load_data, split_data, get_vectorizer

# Global variables to allow other modules to import them
lr_pipeline = None
vectorizer = None

def train_logistic_regression_model(data_path, model_output_path, test_size=0.5, random_state=42):
    global lr_pipeline, vectorizer
    # Load data using your custom data_preprocessing functions
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = split_data(df, test_size=test_size, random_state=random_state)
    
    # Get the TF-IDF vectorizer instance (configured as needed)
    vectorizer = get_vectorizer()
    
    # Create a pipeline that first vectorizes the text then applies Logistic Regression
    lr_pipeline = Pipeline([
        ('tfidf', vectorizer),
        ('clf', LogisticRegression(solver='liblinear'))
    ])
    
    # Train the pipeline on your training data
    lr_pipeline.fit(X_train, y_train)
    
    # Save the trained model pipeline to the specified path
    joblib.dump(lr_pipeline, model_output_path)
    print("Logistic Regression model trained and saved to", model_output_path)
    
    return lr_pipeline, X_test, y_test

if __name__ == "__main__":
    # Train the model using your dataset and save it as 'models/spam_detector.pkl'
    train_logistic_regression_model("data/spam_dataset.csv", "models/spam_detector.pkl")
