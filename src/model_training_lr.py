import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.base import BaseEstimator, TransformerMixin
from data_preprocessing import load_data, split_data, get_vectorizer
# Only import extract_features from feature_engineering
from feature_engineering import extract_features

class FeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Ensure X is a list of strings
        X_str = [str(text) if text is not None else '' for text in X]
        features_df = pd.DataFrame([extract_features(text) for text in X_str])
        return features_df

def train_logistic_regression_model(data_path, model_output_path, test_size=0.2, random_state=42):
    # Load data (it's already cleaned in load_data function)
    df = load_data(data_path)
    
    # Make sure we have enough samples
    print(f"Dataset size: {len(df)} records")
    print(f"Label distribution: {df['label'].value_counts().to_dict()}")
    
    if len(df) < 10:
        print("WARNING: Dataset is too small. Please use a larger dataset.")
        return None, None, None
    
    # Split data (returns already cleaned data)
    X_train, X_test, y_train, y_test = split_data(df, test_size=test_size, random_state=random_state)
    
    # Final check to ensure no NaN values
    X_train = [str(text) if text is not None else '' for text in X_train]
    X_test = [str(text) if text is not None else '' for text in X_test]
    
    # Create pipeline with both text features and engineered features
    # Set a higher weight for engineered features to emphasize spam indicators
    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('text', Pipeline([
                ('tfidf', get_vectorizer())
            ])),
            # Increase the weight of engineered features
            ('engineered', FeatureExtractor())
        ], transformer_weights={
            'text': 1.0,
            'engineered': 2.0  # Give engineered features twice the weight
        })),
        ('clf', LogisticRegression(solver='liblinear', C=1.0, max_iter=1000, class_weight='balanced'))
    ])
    
    # Fit the model
    print("Training the model...")
    pipeline.fit(X_train, y_train)
    
    # Evaluate on test set
    y_pred = pipeline.predict(X_test)
    print("\nModel Evaluation:")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Test with example messages
    print("\nTesting with example messages:")
    examples = [
        "Hey, how are you? Let's meet for coffee tomorrow.",
        "CONGRATULATIONS! You've WON $10,000,000 in our lottery! Click here to claim now!",
        "Your account has been flagged. Please verify your information immediately by clicking this link.",
        "Here's the report you requested for the quarterly meeting."
    ]
    
    for example in examples:
        # Print feature values for spam examples to debug
        features = extract_features(example)
        prediction = pipeline.predict([example])[0]
        
        print(f"Example: {example[:50]}...")
        print(f"Prediction: {prediction}")
        
        # For suspicious examples, print the feature values
        if any(word in example.lower() for word in ['congratulations', 'won', 'click', 'verify']):
            print("Feature values:")
            for k, v in features.items():
                if v > 0:  # Only print non-zero features
                    print(f"  {k}: {v}")
        print()
    
    # Save the model
    joblib.dump(pipeline, model_output_path)
    print(f"Model saved to {model_output_path}")
    
    return pipeline, X_test, y_test

# Let's also create a prediction function that can be used on individual emails
def predict_spam(email_text, model_path):
    """
    Predict if an email is spam or ham using a trained model.
    
    Args:
        email_text (str): The email text to classify
        model_path (str): Path to the trained model file
        
    Returns:
        str: 'spam' or 'ham' prediction
    """
    # Load the trained model
    model = joblib.load(model_path)
    
    # Make prediction
    prediction = model.predict([email_text])[0]
    
    # Print feature values for debugging
    features = extract_features(email_text)
    print("Feature values:")
    for k, v in sorted(features.items(), key=lambda x: x[1], reverse=True)[:10]:
        if v > 0:  # Only print top 10 non-zero features
            print(f"  {k}: {v}")
    
    # Return prediction
    return prediction

if __name__ == "__main__":
    train_logistic_regression_model("data/expanded_spam_dataset.csv", "models/spam_detector.pkl")