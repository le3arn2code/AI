# Interview Q&A: Logistic Regression

1. **Q: What is logistic regression used for?**
   - A: Binary classification tasks where the output is categorical (0/1).

2. **Q: Difference between linear and logistic regression?**
   - A: Linear predicts continuous values, logistic predicts probabilities for classes.

3. **Q: Why use the sigmoid function in logistic regression?**
   - A: To map predictions to probabilities between 0 and 1.

4. **Q: What does the logistic regression coefficient represent?**
   - A: Change in log odds of the outcome per unit increase in predictor.

5. **Q: How do you evaluate logistic regression models?**
   - A: Accuracy, confusion matrix, precision, recall, F1 score, ROC-AUC.

6. **Q: Can logistic regression handle non-linear relationships?**
   - A: Not directly, but adding polynomial terms or feature engineering helps.

7. **Q: What assumptions does logistic regression make?**
   - A: No multicollinearity, linear relationship between features and log odds, large sample size.

8. **Q: How does logistic regression differ from decision trees?**
   - A: Logistic regression assumes linear log odds, decision trees do not assume data distribution.

9. **Q: What happens if dataset is imbalanced?**
   - A: Accuracy may mislead, use precision/recall or resampling methods.

10. **Q: When should logistic regression not be used?**
   - A: When relationship is highly non-linear or when assumptions are violated.
