# Troubleshooting – Lab 07

- **Error: ModuleNotFoundError: No module named 'pandas'**
  ```bash
  pip3 install pandas --break-system-packages
  ```

- **Error: ModuleNotFoundError: No module named 'sklearn'**
  ```bash
  pip3 install scikit-learn --break-system-packages
  ```

- **FutureWarning in Pandas**
  - Avoid chained assignment like `df['col'].fillna(..., inplace=True)`  
  - Use direct assignment: `df['col'] = df['col'].fillna(...)`

