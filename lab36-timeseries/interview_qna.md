# Interview Q&A: Time Series Forecasting

**Q1. What is time series forecasting?**  
A: It is the use of models to predict future values based on previously observed time-stamped data.

**Q2. What are the main components of time series data?**  
A: Trend, seasonality, cyclic patterns, and random noise.

**Q3. Why do we split time series data by time and not randomly?**  
A: Because future observations depend on past ones. Random splits would leak future info into training.

**Q4. What is ARIMA?**  
A: ARIMA stands for AutoRegressive Integrated Moving Average. It models autocorrelation, differencing, and moving average.

**Q5. What do p, d, q represent in ARIMA?**  
A: p = autoregressive terms, d = differencing order, q = moving average terms.

**Q6. Why use Mean Squared Error (MSE) for evaluation?**  
A: MSE penalizes large errors more heavily, making it suitable for forecasting tasks.

**Q7. When would Linear Regression be suitable for time series?**  
A: When data has a simple trend without strong seasonality or autocorrelation.

**Q8. What are the limitations of ARIMA?**  
A: It struggles with non-stationary data with complex seasonality and requires parameter tuning.

**Q9. What is stationarity in time series?**  
A: A stationary series has constant mean, variance, and autocorrelation over time.

**Q10. How do you decide between ARIMA and machine learning models?**  
A: ARIMA is good for small, well-behaved datasets. ML/Deep learning is preferred for large, complex, non-linear datasets.
