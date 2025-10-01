# Troubleshooting for Lab 36

## Issue 1: Missing dataset (FileNotFoundError)
**Error:** `FileNotFoundError: No such file or directory: 'daily_temperatures.csv'`  
**Fix:** Created a synthetic dataset (`daily_temperatures.csv`) programmatically using pandas and numpy.

## Issue 2: FutureWarnings in ARIMA model
**Observation:** Warnings from statsmodels about `no supported index` and covariance matrix.  
**Fix:** Safe to ignore for lab purposes. Added note in README.

