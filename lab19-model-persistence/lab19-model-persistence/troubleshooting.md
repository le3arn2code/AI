# Troubleshooting

- **ModuleNotFoundError: No module named 'joblib'**
  - Install joblib: `pip install joblib`

- **FileNotFoundError: 'random_forest_model.joblib'**
  - Ensure you ran `task2_save_model.py` before running `task3_load_predict.py`.

- **ConvergenceWarnings in training**
  - Not applicable for RandomForestClassifier, but may occur in other models.