import pandas as pd

# Load CSV into DataFrame
df = pd.read_csv("data.csv")

# Show first rows
print("\nHead of dataset:")
print(df.head())

# Show statistics
print("\nStatistics:")
print(df.describe())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Drop missing values
df_cleaned = df.dropna()

# Verify
print("\nAfter cleaning:")
print(df_cleaned.isnull().sum())
