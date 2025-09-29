# Troubleshooting

- **ModuleNotFoundError: No module named 'pandas'**  
  Run:
  ```bash
  pip3 install pandas --break-system-packages
  ```

- **FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'**  
  Ensure `data.csv` is in the same directory as `pandas_lab5.py`.

- **Encoding issues when reading CSV**  
  Use:
  ```python
  pd.read_csv("data.csv", encoding="utf-8")
  ```
