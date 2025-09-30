import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train-validation split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

# Try different tree depths
depth_range = range(1, 10)
train_scores = []
val_scores = []

for depth in depth_range:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    train_scores.append(model.score(X_train, y_train))
    val_scores.append(model.score(X_val, y_val))

# Plot results
plt.plot(depth_range, train_scores, label='Training Score', marker='o')
plt.plot(depth_range, val_scores, label='Validation Score', marker='o')
plt.xlabel('Max Depth')
plt.ylabel('Score')
plt.title('Decision Tree Performance vs. Max Depth')
plt.legend()
plt.savefig("depth_vs_performance.png")  # Save plot to file
print("✅ Plot saved as depth_vs_performance.png")
