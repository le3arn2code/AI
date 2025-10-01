# Troubleshooting - Lab 37 PCA

## Common Issues & Fixes

### 1. ModuleNotFoundError: No module named 'sklearn'
- Ensure scikit-learn is installed in the virtual environment:
  ```bash
  pip install scikit-learn
  ```

### 2. Missing StandardScaler or PCA
- These are part of scikit-learn. Install or upgrade:
  ```bash
  pip install --upgrade scikit-learn
  ```

### 3. Virtual environment not activated
- If `source ~/lab37-venv/bin/activate` is not run, packages won’t be found.

### 4. Plot not showing
- Ensure you are running in an environment with GUI support, or save plots using:
  ```python
  plt.savefig("variance_plot.png")
  ```
