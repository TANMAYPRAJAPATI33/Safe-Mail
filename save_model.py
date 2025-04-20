

import sys
import os
import joblib

this_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(this_dir, 'src')
sys.path.insert(0, src_path)

from src.model_training_lr import train_logistic_regression_model, lr_pipeline

if lr_pipeline is None:
    print("lr_pipeline is None. Training model now...")
    lr_pipeline, _, _ = train_logistic_regression_model("data/spam_dataset.csv", "models/spam_detector.pkl")


vectorizer = lr_pipeline.named_steps['tfidf']

joblib.dump(lr_pipeline, 'models/spam_detector.pkl')
print("Model saved successfully to models/spam_detector.pkl")

joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
print("TF-IDF vectorizer saved successfully to models/tfidf_vectorizer.pkl")
