from sklearn.datasets import load_iris
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Load dataset
iris_data = load_iris()
X = iris_data.data
y = iris_data.target

# Initialize model
model = LogisticRegression(max_iter=200)

# Perform 5-fold cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)

print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean()}")
