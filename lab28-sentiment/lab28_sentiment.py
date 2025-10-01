#!/usr/bin/env python3
# Lab 28: Sentiment Analysis (Concept)

# ===== Task 1: Prepare a Dataset of Labeled Text =====
# 1) Select a Dataset: IMDb movie reviews dataset (file: IMDB Dataset.csv)
# 2) Load and Inspect the Dataset
import pandas as pd

# Load the dataset
df = pd.read_csv('IMDB Dataset.csv')

# Inspect the first few entries
print(df.head())

# 3) Preprocess the Data: remove noise
import re

# Function to clean text
def clean_text(text):
    text = re.sub(r'<[^>]+>', ' ', text)   # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text)    # Remove punctuation
    text = text.lower()                    # Convert to lower case
    return text

df['review'] = df['review'].apply(clean_text)

# ===== Task 2: Use a Simple ML Model for Classification =====
# 1) Data Splitting
from sklearn.model_selection import train_test_split

X = df['review']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 2) Text Vectorization: TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)

# 3) Train a Logistic Regression Model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train_vec, y_train)

# ===== Task 3: Evaluate Accuracy of Sentiment Predictions =====
# 1) Model Evaluation: accuracy score
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# 2) Analyze the Results: (Discuss outside code as per lab instruction)
