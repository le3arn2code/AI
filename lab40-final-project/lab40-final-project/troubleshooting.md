# Troubleshooting Lab 40

1. **ModuleNotFoundError**
   - Install missing dependencies:
     ```bash
     pip3 install pandas scikit-learn
     ```

2. **FileNotFoundError: housing.csv**
   - Ensure dataset is downloaded and unzipped in `~/datasets/california_housing`.

3. **RMSE too high**
   - Try feature engineering (ratios like rooms_per_household, bedrooms_per_room).
   - Use GridSearchCV for better hyperparameters.
