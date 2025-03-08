import sys
import os
import logging
from flask import Flask, request, jsonify
import joblib

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

try:
    # Load the entire pipeline (which includes the TfidfVectorizer)
    model = joblib.load("models/spam_detector.pkl")
    logging.info("Model (pipeline) loaded successfully.")
    logging.info(f"Model type: {type(model)}")
except Exception as e:
    logging.error("Error loading model pipeline: %s", e)
    sys.exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        email_text = data.get("email_text", "")
        if not email_text:
            logging.warning("No email_text provided in request.")
            return jsonify({"error": "No email_text provided."}), 400

        logging.info("Received prediction request for email_text: %s", email_text[:50])
        
        # Pass the raw text directly to the pipeline.
        # The pipeline’s TfidfVectorizer step will handle preprocessing (basic_cleaning).
        prediction = model.predict([email_text])
        logging.info("Prediction: %s", prediction[0])
        
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        logging.exception("Error during prediction:")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
