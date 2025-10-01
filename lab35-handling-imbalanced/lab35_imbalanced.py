import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

# Generate a synthetic imbalanced dataset
X, y = make_classification(
    n_classes=2,
    class_sep=2,
    weights=[0.99, 0.01],
    n_informative=3,
    n_redundant=1,
    flip_y=0,
    n_features=5,
    n_clusters_per_class=1,
    n_samples=1000,
    random_state=42
)

# Convert to DataFrame
data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
data['target'] = y

# Class distribution
print("Class distribution:\n", data['target'].value_counts())

# Split dataset
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Apply SMOTE
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)
print("\nClass distribution after SMOTE:")
print(np.bincount(y_res))

# Train before balancing
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\nClassification Report for Imbalanced Data:\n")
print(classification_report(y_test, y_pred))

# Train after balancing
model_res = LogisticRegression(random_state=42)
model_res.fit(X_res, y_res)
y_pred_res = model_res.predict(X_test)
print("\nClassification Report for Balanced Data (SMOTE applied):\n")
print(classification_report(y_test, y_pred_res))
