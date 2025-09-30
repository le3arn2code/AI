# Interview Q&A - Feature Scaling (Standardization)

1. **Why is feature scaling important in ML?**  
   To ensure features contribute equally and models converge faster.

2. **Difference between normalization and standardization?**  
   - Normalization: scales values between 0–1.  
   - Standardization: mean = 0, std = 1.

3. **Which algorithms are sensitive to feature scaling?**  
   Logistic Regression, SVM, KNN, Neural Networks, K-Means.

4. **Is scaling required for Decision Trees?**  
   No, because they split based on thresholds, not distance.

5. **What happens if you skip scaling in Logistic Regression?**  
   Features with larger ranges dominate coefficient learning.

6. **What’s the math formula for StandardScaler?**  
   `z = (x - mean) / std`

7. **Can we apply scaling after splitting the dataset?**  
   Scaling must be fit on training data, then applied to test data.

8. **How does scaling help in gradient descent?**  
   It speeds up convergence and avoids zig-zag optimization paths.

9. **What are pitfalls of scaling test data separately?**  
   Data leakage – the test set must use training-set parameters.

10. **When would you NOT scale features?**  
    When using tree-based models (Decision Trees, Random Forests, XGBoost).