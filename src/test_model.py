import joblib
from sklearn.metrics import classification_report, confusion_matrix
from data_preprocessing import load_data, split_data

def evaluate_model(model_path, data_path, test_size=0.5, random_state=42):
    model = joblib.load(model_path)
    print("Model loaded from", model_path)
    
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = split_data(df, test_size=test_size, random_state=random_state)
    
    y_pred = model.predict(X_test)
    
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model("models/logistic_regression_model.pkl", "data/expanded_spam_dataset.csv")
