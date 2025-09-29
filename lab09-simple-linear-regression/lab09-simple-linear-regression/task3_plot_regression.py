import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Size': [1500, 1600, 1700, 1800, 1900, 2000, 2100],
    'Price': [250000, 270000, 290000, 310000, 330000, 350000, 370000]
}
df = pd.DataFrame(data)

X = df[['Size']]
y = df['Price']

# Fit model
model = LinearRegression()
model.fit(X, y)

# Plot data points
plt.scatter(X, y, color='blue', label='Data Points')

# Plot regression line
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')

plt.xlabel('Size (sq ft)')
plt.ylabel('Price (USD)')
plt.title('Simple Linear Regression: House Size vs Price')
plt.legend()
plt.savefig("screenshot.png")
print("Plot saved as screenshot.png")
