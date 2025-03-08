# Safe-Mail
# Email Spam Detection System

## Overview
The Email Spam Detection System is a full-cycle machine learning application that classifies emails as spam or ham. Recent improvements include:
- Expanded dataset integration (e.g., SpamAssassin) for better coverage.
- Advanced feature engineering (URL count, suspicious keywords, etc.).
- A unified scikit-learn pipeline (TF-IDF + Logistic Regression) to avoid double preprocessing.
- Docker support for consistent deployment.

## Features
- **Email Preprocessing**  
  - Cleans text (lowercase, remove HTML/punctuation).
  - Optionally performs tokenization, stopword removal, lemmatization.
  - Uses TF-IDF for feature extraction.
- **Model Training & Evaluation**  
  - Logistic Regression (with optional hyperparameter tuning).
  - Evaluation metrics: accuracy, precision, recall, F1-score.
- **API Service**  
  - Flask API at `/predict` for real-time classification (JSON input → JSON output).
  - Comprehensive logging and error handling.
- **Containerization**  
  - Dockerfile provided for building and running the application in a portable environment.

## Technologies Used
- Python 3.11
- Flask
- scikit-learn
- nltk
- joblib
- Docker

## Project Structure
```bash
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
├── Dockerfile                     # Docker container definition
├── convert_spamassassin_to_csv.py # Script to convert SpamAssassin data into CSV
├── requirements.txt               # Python dependencies
├── save_model.py                  # Script to save model/vectorizer
└── README.md                      # Project documentation


## 6. Installation & Setup

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) for containerization.
- Python 3.11 (if running locally without Docker).
- Git (optional, for version control).

### Setting Up the Python Environment (Optional)

If you prefer to run the project locally (without Docker):

1. **Create a Virtual Environment:**

   ```bash
   python3 -m venv "Safe Mail"
   source "Safe Mail/bin/activate"
2. Install Dependencies:

    pip install -r requirements.txt


Docker Setup
Ensure requirements.txt Contains:

    Flask
    joblib
    scikit-learn
    nltk
    pandas

Build the Docker Image:

In the project root (Safe-Mail), run:

    docker build -t safe-mail-app .


Run the Docker Container:
    docker run -p 5001:5001 safe-mail-app  


7. Running the Application
Running the API Locally (Without Docker)
    1.Activate Your Virtual Environment:
        source "Safe Mail/bin/activate"
     
    2.Run the Flask App:
        python3 app.py
    3.Test the API with curl:

        curl -X POST -H "Content-Type: application/json" \
            -d '{"email_text": "Congratulations! You have won a prize. Click here to claim it."}' \
        http://127.0.0.1:5001/predict


Running the API in Docker
1.Build the Docker Image:


    docker build -t safe-mail-app .
2. Run the Docker Container:

    docker run -p 5001:5001 safe-mail-app

3.Test the API with curl:

curl -X POST -H "Content-Type: application/json" \
     -d '{"email_text": "Congratulations! You have won a prize. Click here to claim it."}' \
     http://127.0.0.1:5001/predict


8. API Details
Endpoint: /predict
Method: POST
Request Payload:
JSON with the key "email_text"

json
    {
    "email_text": "Congratulations! You have won a prize. Click here to claim it."
    }
Response:
JSON with the prediction

    json
    {
    "prediction": "ham"
    }


9. Logging & Error Handling
The Flask API logs every incoming request and its corresponding prediction.
Errors during processing are captured and logged, and appropriate HTTP status codes are returned.
Logs are output both to the console and an app.log file in the project root for debugging and monitoring.


--
10. Future Enhancements

Model Improvements:
1. Expand the dataset further (e.g., incorporating SpamAssassin or Enron).
2. Experiment with additional classifiers (SVM, Random Forest, neural networks).
3. Enhance feature engineering (e.g., using pre-trained embeddings or transformer-based models).

Gmail Integration:
- Develop a Gmail extension or add-on to automatically flag spam emails in Gmail.

Production Deployment:
- Deploy the containerized application using a production-grade WSGI server (e.g., Gunicorn) behind a reverse proxy (e.g., Nginx).

Monitoring:
- Integrate tools for monitoring API usage and model performance over time (logging dashboards, metrics collection).

11. Summary

The Email Spam Detection System:
- Cleans, preprocesses, and vectorizes email text using TF-IDF.
- Trains and evaluates a Logistic Regression model (with optional hyperparameter tuning) for spam/ham classification.
- Provides a Flask-based REST API (`/predict`) for real-time spam detection.
- Offers Docker containerization for consistent, portable deployment.

This setup ensures a robust foundation for continued enhancements, including expanded datasets, advanced classifiers, and seamless production deployments.


This **README.md** file contains all sections neatly arranged, from introduction and installation steps to API usage, logging, and future enhancements. You can use this for documentation or present it as is. Let me know if you'd like any further changes!
