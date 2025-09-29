# Troubleshooting – Lab 08

- **Error: ModuleNotFoundError (NumPy, Pandas, scikit-learn, Matplotlib)**  
  Install missing library with:  
  ```bash
  pip3 install <library> --break-system-packages
  ```

- **Matplotlib window hangs in server/VM**  
  Use non-interactive backend with:  
  ```python
  import matplotlib
  matplotlib.use("Agg")
  ```

- **Accuracy is very low for k-NN**  
  - Check dataset split.  
  - Try different `n_neighbors` values.
