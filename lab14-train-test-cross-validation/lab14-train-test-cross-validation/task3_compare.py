from sklearn.datasets import load_iris
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score

# Load dataset
iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['target'] = iris_data.target

X = df.drop('target', axis=1)
y = df['target']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize model
model = LogisticRegression(max_iter=200)

# Train-test split evaluation
model.fit(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Test score (train-test split): {test_score}")

# Cross-validation evaluation
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean()}")

print("\nKey Observations:")
print("- Train-test split provides a single performance estimate which might be high variance.")
print("- Cross-validation uses multiple splits to provide a more stable estimation of model performance.")
