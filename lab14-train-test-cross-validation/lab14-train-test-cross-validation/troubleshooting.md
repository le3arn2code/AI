# Troubleshooting Guide for Lab 14

1. **ModuleNotFoundError: No module named 'sklearn'**
   - Install scikit-learn: `pip install scikit-learn`

2. **ValueError: Solver failed to converge**
   - Increase max_iter in LogisticRegression: `LogisticRegression(max_iter=500)`

3. **Dataset not found**
   - Ensure `load_iris()` is imported from `sklearn.datasets`.

4. **Different accuracy scores**
   - Scores may vary slightly due to random_state. Use `random_state=42` for consistency.
