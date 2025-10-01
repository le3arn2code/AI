# Lab 33: Hyperparameter Tuning with GridSearchCV

## Layman's Explanation
This lab focused on **tuning machine learning models** automatically instead of guessing the best settings. 
Think of it like adjusting the knobs on a washing machine – GridSearchCV tests different settings (water temperature, spin speed) 
and finds the combination that cleans clothes best. Here, we tested **SVM hyperparameters** and found the best set.

We used the **Iris dataset**, tried multiple combinations of hyperparameters (`C`, `gamma`, `kernel`) 
and let GridSearchCV test them all. The result was a **perfect classifier** with 100% accuracy.

## Steps Completed
1. Installed and verified required software (Python3, NumPy, Pandas, Scikit-learn).
2. Defined a parameter grid with different SVM hyperparameters.
3. Ran `GridSearchCV` with cross-validation on the Iris dataset.
4. Printed the best parameters and evaluated the model with a classification report and confusion matrix.

## Errors Faced and Resolutions
- **Software mismatch**: We used Ubuntu 24.04, so all installations were done with the `--break-system-packages` method for pip.
- **Resolution**: Verified with `python3 -c "import numpy, pandas, sklearn"` that all libraries were installed successfully.

## Final Result
- **Best Parameters**: `C=100, gamma=0.01, kernel='rbf'`
- **Performance**: 100% accuracy, perfect classification report, and confusion matrix with no misclassifications.

