# model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# 1. Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')

# 2. Split into X and y
X = data["text"]
y = data["label"]

# 3. Convert text into numbers (TF-IDF)
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 4. Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

# 5. Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")