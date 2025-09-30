# Lab 17 Interview Q&A

1. What is feature importance in Random Forest?
   - A score that reflects how much each feature contributes to predictions.

2. Why is feature selection important?
   - It reduces overfitting, improves model performance, and speeds up training.

3. How do Random Forests calculate feature importance?
   - By measuring how much each feature decreases impurity across trees.

4. What happens if you remove too many features?
   - The model may lose predictive power (underfitting).

5. What is dimensionality reduction?
   - Reducing the number of features, either via feature selection or transformations like PCA.

6. How do you choose a threshold for importance?
   - Often empirically, e.g., 0.05, or via domain knowledge.

7. Can low-importance features still be useful?
   - Sometimes in interactions with other features.

8. What’s the difference between PCA and feature selection?
   - PCA transforms features; feature selection keeps original features but filters them.

9. Why use Random Forest for feature selection?
   - It is robust, handles non-linearities, and works well with mixed feature types.

10. What if different runs give different rankings?
   - Set `random_state` for reproducibility, or average across multiple runs.
