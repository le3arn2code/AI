# Interview Q&A: Train-Test Split & Cross-Validation

1. **Why do we split datasets into training and testing sets?**
   - To evaluate how well a model generalizes to unseen data.

2. **What’s the disadvantage of a simple train-test split?**
   - It gives a single performance estimate, which may have high variance.

3. **How does cross-validation solve this issue?**
   - By averaging results across multiple folds, reducing variance in performance estimates.

4. **What is k in k-fold cross-validation?**
   - It defines the number of splits. Each fold is used once as a test set.

5. **What happens if k is too small or too large?**
   - Too small: high variance; too large (like LOOCV): high computational cost.

6. **When would you prefer train-test split over cross-validation?**
   - For very large datasets, train-test split is quicker and sufficient.

7. **Can cross-validation help with hyperparameter tuning?**
   - Yes, it’s commonly used in grid search and model selection.

8. **What’s stratified cross-validation?**
   - Ensures that each fold has the same proportion of classes as the dataset.

9. **Why is random_state important in splitting?**
   - It ensures reproducibility of results.

10. **What is the trade-off between bias and variance in validation?**
   - Train-test split may have high variance. Cross-validation reduces variance but may introduce slight bias due to repeated sampling.
