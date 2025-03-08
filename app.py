import sys
import os
import logging
from flask import Flask, request, jsonify
import joblib

this_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(this_dir, 'src')
sys.path.insert(0, src_path)

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

app = Flask(__name__)

try:
    model = joblib.load("models/tuned_logistic_regression_model.pkl")
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error("Error loading model: %s", e)
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
        prediction = model.predict([email_text])
        logging.info("Prediction: %s", prediction[0])
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        logging.exception("Error during prediction:")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
