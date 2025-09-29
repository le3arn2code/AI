import pandas as pd

# Create a small dataset
data = {
    'Size': [1500, 1600, 1700, 1800, 1900, 2000, 2100],
    'Price': [250000, 270000, 290000, 310000, 330000, 350000, 370000]
}
df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())
