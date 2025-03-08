
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate

from advanced_preprocessing import preprocess
from feature_engineering import extract_features

df = pd.read_csv('data/expanded_spam_dataset.csv')

df['clean_text'] = df['text'].apply(preprocess)

features_df = df['text'].apply(extract_features).apply(pd.Series)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X_tfidf = vectorizer.fit_transform(df['clean_text'])

X_combined = hstack([X_tfidf, features_df.values])


y = df['label']

clf = RandomForestClassifier(n_estimators=100, random_state=42)

cv_results = cross_validate(clf, X_combined, y, cv=3, scoring='f1_macro', return_train_score=True)

print("Cross-validation F1 macro scores:", cv_results['test_score'])
print("Average F1 macro score: {:.2f}".format(cv_results['test_score'].mean()))
