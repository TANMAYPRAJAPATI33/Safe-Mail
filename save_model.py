# save_model.py

import sys
import os
import joblib

# Add the 'src' directory to the Python path so that modules inside 'src' can be imported.
this_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(this_dir, 'src')
sys.path.insert(0, src_path)

# Import the training function and the global variable from model_training_lr.py
from src.model_training_lr import train_logistic_regression_model, lr_pipeline

# If lr_pipeline is None, then the training function hasn't been run; so run it.
if lr_pipeline is None:
    print("lr_pipeline is None. Training model now...")
    lr_pipeline, _, _ = train_logistic_regression_model("data/spam_dataset.csv", "models/spam_detector.pkl")

# Now, extract the vectorizer from the trained pipeline.
# This assumes your pipeline was built as [('tfidf', vectorizer), ('clf', ...)]
vectorizer = lr_pipeline.named_steps['tfidf']

# Save the trained model pipeline to the models directory.
joblib.dump(lr_pipeline, 'models/spam_detector.pkl')
print("Model saved successfully to models/spam_detector.pkl")

# Save the TF-IDF vectorizer to the models directory.
joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
print("TF-IDF vectorizer saved successfully to models/tfidf_vectorizer.pkl")
