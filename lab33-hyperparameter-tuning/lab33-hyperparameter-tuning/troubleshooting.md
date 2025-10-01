# Troubleshooting - Lab 33: Hyperparameter Tuning with GridSearchCV

## Common Issues and Fixes

### 1. Software mismatch error on Ubuntu 24.04
- **Error**: Cannot install scikit-learn with pip (externally-managed-environment).
- **Fix**: Use `--break-system-packages` flag to force install.

### 2. Import Errors (numpy, pandas, sklearn not found)
- **Fix**: Verify installation with:
  ```bash
  python3 -c "import numpy, pandas, sklearn; print('✅ All libraries installed successfully')"
  ```

### 3. High computation time (for larger datasets)
- **Fix**: Use `RandomizedSearchCV` or reduce parameter grid size.

