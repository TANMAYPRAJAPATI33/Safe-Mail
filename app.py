import sys
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

from src.feature_engineering import FeatureExtractor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)
CORS(app)

print("Starting Spam Detector Flask App...")

# Load model with error handling
model_path = "models/spam_detector.pkl"
try:
    if not os.path.exists(model_path):
        logging.error(f"Model file not found: {model_path}")
        sys.exit(1)
    
    model = joblib.load(model_path)
    logging.info("Model loaded successfully.")
    logging.info(f"Model type: {type(model)}")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    sys.exit(1)

@app.route('/predict', methods=['OPTIONS', 'POST'])
def predict():
    if request.method == 'OPTIONS':
        return '', 200

    try:
        data = request.get_json(force=True)
        email_text = data.get("email_text", "")

        if not email_text:
            logging.warning("No email_text provided in request.")
            return jsonify({"error": "No email_text provided."}), 400

        logging.info(f"Prediction request for: {email_text[:60]}...")

        try:
            pred_proba = model.predict_proba([email_text])[0]
            prediction = model.predict([email_text])[0]

            classes = model.classes_ if hasattr(model, 'classes_') else ['ham', 'spam']
            spam_idx = 1 if 'spam' in classes else 0
            ham_idx = 0 if 'ham' in classes else 1

            result = {
                "prediction": prediction,
                "spam_probability": float(pred_proba[spam_idx]),
                "ham_probability": float(pred_proba[ham_idx])
            }

            logging.info(f"Prediction: {prediction}, Spam prob: {result['spam_probability']:.4f}")
            return jsonify(result)

        except AttributeError:
            prediction = model.predict([email_text])[0]
            logging.info(f"Prediction: {prediction}")
            return jsonify({"prediction": prediction})

    except Exception as e:
        logging.exception("Prediction error:")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
