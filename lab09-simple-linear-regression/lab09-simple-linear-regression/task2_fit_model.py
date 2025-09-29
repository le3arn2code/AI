import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Size': [1500, 1600, 1700, 1800, 1900, 2000, 2100],
    'Price': [250000, 270000, 290000, 310000, 330000, 350000, 370000]
}
df = pd.DataFrame(data)

# Features and target
X = df[['Size']]
y = df['Price']

# Fit model
model = LinearRegression()
model.fit(X, y)

# Coefficient & intercept
print(f"Coefficient (Slope): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
