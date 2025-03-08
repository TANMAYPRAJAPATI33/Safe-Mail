# Safe-Mail
# Email Spam Detection System

## Overview

The Email Spam Detection System is a full-cycle machine learning application that identifies whether an email is spam or not. The system:

- **Preprocesses Email Data:** Loads, cleans, and converts email text into numerical features using TF-IDF.
- **Trains a Classification Model:** Uses Logistic Regression (with hyperparameter tuning via GridSearchCV) to classify emails as "spam" or "ham".
- **Provides an API:** Exposes a RESTful `/predict` endpoint via a Flask application, which processes email text and returns predictions.
- **Uses Docker for Containerization:** Packages the entire application (code, model, and dependencies) into a Docker container for consistent and portable deployment.
- **Includes Logging & Error Handling:** Tracks requests and predictions, with detailed logs for debugging and monitoring.

This project serves as a strong foundation for further improvements and integrations, such as developing a Gmail extension for real-time spam detection.

## Features

- **Email Preprocessing:**  
  - Cleaning (converting to lowercase, removing HTML tags and punctuation).  
  - TF-IDF vectorization for feature extraction.
  
- **Model Training & Evaluation:**  
  - Baseline and tuned Logistic Regression classifier using GridSearchCV.
  - Evaluation using metrics like accuracy, precision, recall, F1-score, and a confusion matrix.

- **API Service:**  
  - Flask API with a `/predict` endpoint that accepts email text (in JSON format) and returns a spam/ham prediction.
  - Robust logging and error handling.

- **Containerization:**  
  - Dockerfile provided to build an image containing the entire application for seamless deployment.

## Technologies Used

- Python 3.11
- Flask
- scikit-learn
- nltk
- joblib
- Docker


## 5. Project Structure

```bash
Safe-Mail/
├── data/
│   └── spam_dataset.csv        # Sample dataset with email text and labels
├── models/                     # Directory for storing trained model files
├── src/
│   ├── __init__.py             # (Optional) Makes src a Python package
│   ├── data_preprocessing.py   # Functions for loading, cleaning, and vectorizing email data
│   ├── model_training.py       # Baseline model training script
│   ├── model_training_lr.py    # Logistic Regression training with hyperparameter tuning
│   └── test_model.py           # Model evaluation script
├── app.py                      # Flask API serving model predictions
├── Dockerfile                  # Dockerfile for containerizing the application
├── requirements.txt            # List of Python dependencies
└── README.md                   # This documentation guide


---

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

Expand the dataset (e.g., incorporating SpamAssassin or Enron datasets).
Experiment with additional classifiers (SVM, Random Forest, or neural networks).
Enhance feature engineering (e.g., using pre-trained embeddings or transformer-based models).
Gmail Integration:

Develop a Gmail extension or add-on to automatically flag spam emails in Gmail.
Production Deployment:

Deploy the containerized application using a production-grade WSGI server (e.g., Gunicorn) behind a reverse proxy (e.g., Nginx).
Monitoring:

Integrate tools for monitoring API usage and model performance over time.

11. Summary
The Email Spam Detection System:

Preprocesses and vectorizes email text.
Trains and evaluates a machine learning model (Logistic Regression) to classify emails as spam or ham.
Provides a REST API for predictions via a Flask application.
Runs within a Docker container for consistent, portable deployment


This **README.md** file contains all sections neatly arranged, from introduction and installation steps to API usage, logging, and future enhancements. You can use this for documentation or present it as is. Let me know if you'd like any further changes!
