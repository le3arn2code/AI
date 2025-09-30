# Troubleshooting - Lab 17

## Common Issues
- **ModuleNotFoundError: scikit-learn**
  - Run: `pip install scikit-learn`
- **Matplotlib not displaying plots**
  - Ensure you're running in an environment with GUI or Jupyter.
- **Accuracy varies**
  - RandomForestClassifier uses randomness. Use `random_state=42` for reproducibility.
