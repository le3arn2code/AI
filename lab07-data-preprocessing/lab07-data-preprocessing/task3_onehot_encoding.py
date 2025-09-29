import pandas as pd

# Sample dataset
data = {
    "Employee": ["A", "B", "C", "D"],
    "Department": ["HR", "Engineering", "Finance", "HR"]
}

df = pd.DataFrame(data)
print("\nOriginal Dataset:")
print(df)

# Apply One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=["Department"])

print("\nAfter One-Hot Encoding:")
print(df_encoded)
