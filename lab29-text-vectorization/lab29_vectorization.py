#!/usr/bin/env python3
# Lab Name: Text Vectorization (Bag-of-Words, TF-IDF)

# ----- Task 1: Implement a Bag-of-Words Approach -----
# Step 1: Import Necessary Libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Step 2: Prepare the Text Data
documents = [
    'I love machine learning.',
    'Machine learning is amazing.',
    'I love creating machine learning models.',
    'Models are crucial for predictive analytics.'
]

# Step 3: Apply CountVectorizer (Bag-of-Words)
vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(documents)

print("Feature Names:", vectorizer.get_feature_names_out())
print("Bag-of-Words Matrix:\n", X_bow.toarray())

# ----- Task 2: Compare it with TF-IDF Vectorization -----
# Step 1: Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 2: Apply TfidfVectorizer to the Same Dataset
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(documents)

print("TF-IDF Feature Names:", tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Matrix:\n", X_tfidf.toarray())

# ----- Task 3: Train a Simple Classifier and Compare Results -----
# Step 1: Import the Necessary Classifier and Dataset Tools
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Step 2: Create a Simple Dataset with Labels
labels = [1, 1, 1, 0]  # 1 represents positive sentiment, 0 represents neutral sentiment

# Step 3: Train-Test Split
X_train_bow, X_test_bow, y_train, y_test = train_test_split(
    X_bow, labels, test_size=0.2, random_state=42
)
X_train_tfidf, X_test_tfidf = train_test_split(
    X_tfidf, test_size=0.2, random_state=42
)

# Step 4: Train a Naive Bayes Classifier Using Bag-of-Words
clf_bow = MultinomialNB()
clf_bow.fit(X_train_bow, y_train)
y_pred_bow = clf_bow.predict(X_test_bow)
print("Bag-of-Words Naive Bayes Accuracy:", metrics.accuracy_score(y_test, y_pred_bow))

# Step 5: Train the Same Classifier Using TF-IDF
clf_tfidf = MultinomialNB()
clf_tfidf.fit(X_train_tfidf, y_train)
y_pred_tfidf = clf_tfidf.predict(X_test_tfidf)
print("TF-IDF Naive Bayes Accuracy:", metrics.accuracy_score(y_test, y_pred_tfidf))
