import pandas as pd
import numpy as np

# Load sample dataset
df = pd.read_csv('sample_data.csv')

print("\nOriginal Dataset:")
print(df)

# Identify missing data
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows with missing values
df_dropped = df.dropna()
print("\nAfter Dropping Missing Values (rows):")
print(df_dropped)

# Fill missing values
df_filled = df.copy()
df_filled["Age"] = df["Age"].fillna(df["Age"].mean())
df_filled["Department"] = df["Department"].fillna("Unknown")

print("\nAfter Filling Missing Values:")
print(df_filled)
