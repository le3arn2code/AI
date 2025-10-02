# Lab 40: Final Mini AI Project
# California Housing Prices

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
print("=== Loading dataset ===")
df = pd.read_csv("datasets/california_housing/housing.csv")
df = pd.get_dummies(df, columns=['ocean_proximity'])
print("First 5 rows:\n", df.head())

# Handle missing values
print("\n=== Missing values before cleaning ===")
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
print("Missing values handled.")

# Feature Engineering
print("\n=== Feature Engineering ===")
scaler = StandardScaler()
df['median_income_scaled'] = scaler.fit_transform(df[['median_income']])
print("Added scaled feature: median_income_scaled")

# Split dataset
X = df.drop('median_house_value', axis=1)
y = df['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split into train/test sets.")

# Train model
print("\n=== Training Model ===")
model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(X_train, y_train)
print("Model training complete.")

# Evaluate
print("\n=== Model Evaluation ===")
predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions) ** 0.5
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

print("\n=== Lab 40 Complete ===")
