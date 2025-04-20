import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from data_preprocessing import load_data, split_data, get_vectorizer

def tune_logistic_regression_model(data_path, model_output_path, test_size=0.2, random_state=42):
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = split_data(df, test_size=test_size, random_state=random_state)
    
   
    vectorizer = get_vectorizer()
    pipeline = Pipeline([
        ('tfidf', vectorizer),
        ('clf', LogisticRegression(solver='liblinear'))
    ])
    
    
    param_grid = {
        'clf__C': [0.01, 0.1, 1, 10],
        'clf__penalty': ['l1', 'l2']
    }
    
    grid = GridSearchCV(pipeline, param_grid, cv=2, scoring='f1_macro')
    grid.fit(X_train, y_train)
    
    print("Best parameters found:", grid.best_params_)
    print("Best cross-validation score:", grid.best_score_)
    
    best_model = grid.best_estimator_
    joblib.dump(best_model, model_output_path)
    print("Tuned model saved to", model_output_path)
    
    return best_model, X_test, y_test

if __name__ == "__main__":
    tune_logistic_regression_model("data/expanded_spam_dataset.csv", "models/tuned_logistic_regression_model.pkl")
