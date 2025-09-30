# Troubleshooting Guide - Lab 16

### Common Issues

1. **ModuleNotFoundError: No module named 'sklearn'**
   - Fix: Install scikit-learn using `pip install scikit-learn`.

2. **ConvergenceWarning in Logistic Regression**
   - Fix: Increase iterations with `LogisticRegression(max_iter=500)`.

3. **Accuracy remains low**
   - Cause: Random synthetic dataset may not always separate classes well.
   - Fix: Increase dataset size or use real-world data.

4. **Pandas / Numpy not installed**
   - Fix: `pip install pandas numpy`.

5. **Permission errors when installing packages**
   - Fix: Use virtual environment:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```