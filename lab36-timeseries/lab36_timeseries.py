import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# --- Generate synthetic daily temperature dataset ---
dates = pd.date_range(start="2022-01-01", end="2023-12-31", freq="D")
temperature = 10 + 15 * np.sin(np.linspace(0, 6.3, len(dates))) + np.random.normal(0, 2, len(dates))
data = pd.DataFrame({"Date": dates, "Temperature": temperature})
data.to_csv("daily_temperatures.csv", index=False)

# --- Load dataset ---
data = pd.read_csv("daily_temperatures.csv", parse_dates=["Date"], index_col="Date")
print("First few rows of dataset:\n", data.head())

# --- Plot the dataset ---
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["Temperature"])
plt.title("Daily Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()

# --- Split dataset ---
train_data = data[:'2022']
test_data = data['2023':]
print("Training data length:", len(train_data))
print("Testing data length:", len(test_data))

# --- ARIMA Model ---
model = ARIMA(train_data["Temperature"], order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=len(test_data))

plt.plot(test_data.index, test_data["Temperature"], label="Actual")
plt.plot(test_data.index, forecast, label="Forecast (ARIMA)", color="red")
plt.legend()
plt.show()

mse_arima = mean_squared_error(test_data, forecast)
print("Mean Squared Error (ARIMA):", mse_arima)
print("\nARIMA Model Summary:\n", model_fit.summary())

# --- Linear Regression Model ---
train_days = np.array(range(len(train_data))).reshape(-1, 1)
test_days = np.array(range(len(train_data), len(train_data) + len(test_data))).reshape(-1, 1)

linear_model = LinearRegression()
linear_model.fit(train_days, train_data["Temperature"])
predictions = linear_model.predict(test_days)

plt.plot(test_data.index, test_data["Temperature"], label="Actual")
plt.plot(test_data.index, predictions, label="Prediction (Linear Regression)", color="red")
plt.legend()
plt.show()

mse_lr = mean_squared_error(test_data, predictions)
print("Mean Squared Error (Linear Regression):", mse_lr)
