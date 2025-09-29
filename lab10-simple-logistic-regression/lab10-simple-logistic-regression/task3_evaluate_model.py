import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Dataset
data = {
    'study_hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'pass_fail': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

X = df[['study_hours']]
y = df['pass_fail']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Coefficients
coeff = model.coef_[0][0]
intercept = model.intercept_[0]
print(f"Coefficient: {coeff}")
print(f"Intercept: {intercept}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Decision Boundary Plot
plt.scatter(X_test, y_test, color='red', label='Test Data')
plt.plot(X_test, model.predict_proba(X_test)[:, 1], color='blue', linewidth=2, label='Decision Boundary')
plt.xlabel('Study Hours')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression Decision Boundary')
plt.legend()
plt.savefig("screenshot.png")
print("✅ Decision boundary saved as screenshot.png")
