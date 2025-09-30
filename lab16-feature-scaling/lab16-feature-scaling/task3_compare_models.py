import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create synthetic dataset
data = {
    'Feature1': np.random.randint(0, 100, 100),
    'Feature2': np.random.randint(100, 200, 100),
    'Target': np.random.choice([0, 1], 100)
}
df = pd.DataFrame(data)

# Separate features and target
X = df[['Feature1', 'Feature2']]
y = df['Target']

# Train-test split on unscaled data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression without scaling
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
original_accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy without scaling: {original_accuracy:.2f}")

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

# Train-test split on scaled data
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(
    X_scaled_df, y, test_size=0.2, random_state=42)

# Train logistic regression with scaling
model_scaled = LogisticRegression(max_iter=200)
model_scaled.fit(X_train_scaled, y_train_scaled)
y_pred_scaled = model_scaled.predict(X_test_scaled)
scaled_accuracy = accuracy_score(y_test_scaled, y_pred_scaled)
print(f"Accuracy with scaling: {scaled_accuracy:.2f}")