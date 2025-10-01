# Interview Q&A - Lab 33: Hyperparameter Tuning with GridSearchCV

### Q1: What is hyperparameter tuning?
**A1:** Hyperparameter tuning is the process of finding the best settings (parameters) for a model that are not learned from data, e.g., `C` and `gamma` in SVM.

### Q2: Why is GridSearchCV used?
**A2:** It automates the search across a predefined grid of hyperparameters, ensuring we find the best combination without manual trial and error.

### Q3: What does `C` mean in SVM?
**A3:** `C` is the regularization parameter that controls the trade-off between a smooth decision boundary and classifying training points correctly.

### Q4: What does `gamma` do in SVM?
**A4:** `gamma` defines how far the influence of a single training example reaches. Low values = broader influence, high values = tighter influence.

### Q5: Why use cross-validation in GridSearchCV?
**A5:** To avoid overfitting and ensure that the chosen hyperparameters generalize well to unseen data.

### Q6: What is the difference between GridSearchCV and RandomizedSearchCV?
**A6:** GridSearchCV exhaustively tries all parameter combinations, while RandomizedSearchCV tests a fixed number of random combinations (faster).

### Q7: Why did we use the Iris dataset here?
**A7:** It is small, well-labeled, and commonly used for ML demonstrations, making it ideal for quick experimentation.

### Q8: What was the final best parameter combination in this lab?
**A8:** `C=100, gamma=0.01, kernel='rbf'`

### Q9: What would you do if GridSearchCV takes too long?
**A9:** Use fewer parameters, RandomizedSearchCV, or advanced methods like Bayesian Optimization.

### Q10: Can GridSearchCV be parallelized?
**A10:** Yes, it supports `n_jobs=-1` to use all CPU cores for faster execution.

