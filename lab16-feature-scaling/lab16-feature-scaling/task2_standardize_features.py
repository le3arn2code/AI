import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create sample dataset
data = {
    'Feature1': np.random.randint(0, 100, 100),
    'Feature2': np.random.randint(100, 200, 100),
    'Target': np.random.choice([0, 1], 100)
}
df = pd.DataFrame(data)

print("Original Dataset Sample:")
print(df.head())

# Separate features
X = df[['Feature1', 'Feature2']]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

print("\nStandardized Features Sample:")
print(X_scaled_df.head())