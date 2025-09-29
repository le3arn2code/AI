import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample dataset
data = {
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": [3000, 4500, 7000, 5500, 8000]
}

df = pd.DataFrame(data)
print("\nOriginal Dataset:")
print(df)

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Normalize Salary column
df["Normalized_Salary"] = scaler.fit_transform(df[["Salary"]])

print("\nAfter Normalization (Min-Max Scaling):")
print(df)
