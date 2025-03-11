cat <<'EOF' > README.md
# Safe-Mail

# Email Spam Detection System

# 1. Overview
The Email Spam Detection System is a full-cycle machine learning application that classifies emails as spam or ham. Recent improvements include:
- Expanded dataset integration (e.g., SpamAssassin) for better coverage.
- Advanced feature engineering (URL count, suspicious keywords, etc.).
- A unified scikit-learn pipeline (TF-IDF + Logistic Regression) to avoid double preprocessing.
- Docker support for consistent deployment.

# 2. Features

## 2.1 Email Preprocessing
- Cleans text (lowercase, remove HTML/punctuation).
- Optionally performs tokenization, stopword removal, lemmatization.
- Uses TF-IDF for feature extraction.

## 2.2 Model Training & Evaluation
- Logistic Regression (with optional hyperparameter tuning).
- Evaluation metrics: accuracy, precision, recall, F1-score.

## 2.3 API Service
- A Flask API at `/predict` for real-time classification (JSON input → JSON output).
- Comprehensive logging and error handling.

## 2.4 Automated Email Classification (IMAP)
- `process_emails.py` connects to your Gmail inbox via IMAP.
- Classifies unread emails using the same model pipeline.
- Moves or deletes spam automatically based on confidence thresholds.
- Credentials stored securely in a `.env` file (ignored by Git).

## 2.5 Containerization
- A Dockerfile is provided for building and running the application in a portable environment.

# 3. Technologies Used
- Python 3.11
- Flask
- scikit-learn
- nltk
- joblib
- Docker

# 4. Project Structure
Safe-Mail/
├── data/
│   ├── spamassassin/              # Contains ham/spam from SpamAssassin
│   ├── expanded_spam_dataset.csv  # Combined dataset (SpamAssassin, etc.)
│   └── spam_dataset.csv           # Original small dataset
├── models/
│   ├── spam_detector.pkl          # Final trained model pipeline
│   └── tfidf_vectorizer.pkl       # (If separately saved)
├── src/
│   ├── __init__.py                # Makes src a Python package (optional)
│   ├── data_preprocessing.py      # Basic data loading/cleaning
│   ├── advanced_preprocessing.py  # Advanced text processing
│   ├── feature_engineering.py     # Additional numeric feature extraction
│   ├── model_training_lr.py       # Logistic Regression pipeline training
│   ├── model_training_advanced.py # Advanced training script
│   ├── model_tuning_lr.py         # Hyperparameter tuning
│   └── test_model.py              # Model evaluation
├── app.py                         # Flask API
├── process_emails.py             # IMAP-based email classification script
├── Dockerfile                     # Docker container definition
├── convert_spamassassin_to_csv.py # Script to convert SpamAssassin data into CSV
├── requirements.txt               # Python dependencies
├── save_model.py                  # Script to save model/vectorizer
└── README.md                      # Project documentation

# 5. Installation & Setup

## 5.1 Prerequisites
1. [Docker Desktop](https://www.docker.com/products/docker-desktop/) for containerization.
2. Python 3.11 (if running locally without Docker).
3. Git (optional, for version control).

# 5.2 Setting Up the Python Environment (Optional)
If you prefer to run the project locally (without Docker):
1. Create a Virtual Environment:
   python3 -m venv "Safe Mail"
   source "Safe Mail/bin/activate"
2. Install Dependencies:
   pip install -r requirements.txt

# 5.3 Docker Setup
Ensure requirements.txt contains:
Flask
joblib
scikit-learn
nltk
pandas

Build the Docker Image:
  docker build -t safe-mail-app .

Run the Docker Container:
  docker run -p 5001:5001 safe-mail-app

# 6. Running the Application

# 6.1 Running the API Locally (Without Docker)
1. Activate Your Virtual Environment:
   source "Safe Mail/bin/activate"
2. Run the Flask App:
   python3 app.py
3. Test the API with curl:
   curl -X POST -H "Content-Type: application/json" \
        -d '{"email_text": "Congratulations! You have won a prize. Click here to claim it."}' \
        http://127.0.0.1:5001/predict

# 6.2 Running the API in Docker
1. Build the Docker Image:
   docker build -t safe-mail-app .
2. Run the Docker Container:
   docker run -p 5001:5001 safe-mail-app
3. Test the API with curl:
   curl -X POST -H "Content-Type: application/json" \
        -d '{"email_text": "Congratulations! You have won a prize. Click here to claim it."}' \
        http://127.0.0.1:5001/predict

# 6.3 Running the IMAP Email Classification Script
To automatically classify unread emails in your Gmail account, run:
  python process_emails.py

# 7. API Details

# 7.1 Endpoint
/predict (POST method)

# 7.2 Request Payload
JSON with the key "email_text":
{
  "email_text": "Congratulations! You have won a prize. Click here to claim it."
}

# 7.3 Response
JSON with the prediction:
{
  "prediction": "ham"
}

# 8. Logging & Error Handling
The Flask API logs every incoming request and its corresponding prediction.
Errors during processing are captured and logged, and appropriate HTTP status codes are returned.
Logs are output both to the console and an app.log file in the project root for debugging and monitoring.

# 9. IMAP-Based Automatic Classification
process_emails.py uses IMAP to connect to your Gmail account.
Classifies unread emails using the same spam detection model.
Moves or deletes spam emails based on defined confidence thresholds.


# 10. Future Enhancements

# 10.1 Model Improvements
1. Expand the dataset further (e.g., incorporating SpamAssassin or Enron).
2. Experiment with additional classifiers (SVM, Random Forest, neural networks).
3. Enhance feature engineering (e.g., using pre-trained embeddings or transformer-based models).

# 10.2 Gmail Integration
Develop a Gmail extension or add-on to automatically flag spam emails in Gmail.

# 10.3 Production Deployment
Deploy the containerized application using a production-grade WSGI server (e.g., Gunicorn) behind a reverse proxy (e.g., Nginx).

# 10.4 Monitoring
Integrate tools for monitoring API usage and model performance over time (logging dashboards, metrics collection).

# 11. Summary
The Email Spam Detection System:
- Cleans, preprocesses, and vectorizes email text using TF-IDF.
- Trains and evaluates a Logistic Regression model (with optional hyperparameter tuning) for spam/ham classification.
- Provides a Flask-based REST API (/predict) for real-time spam detection.
- Offers Docker containerization for consistent, portable deployment.
- Includes an IMAP script (process_emails.py) to automatically classify unread emails in Gmail.

This setup ensures a robust foundation for continued enhancements, including expanded datasets,
advanced classifiers, and seamless production deployments.

