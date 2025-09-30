# Interview Q&A: Early Stopping and Regularization

1. **What is early stopping?**
   - A regularization technique that halts training when validation performance stops improving.

2. **Why use L2 regularization?**
   - It penalizes large weights, reducing model complexity and overfitting.

3. **Difference between L1 and L2 regularization?**
   - L1 encourages sparsity (feature selection), L2 shrinks weights evenly.

4. **How does early stopping help with generalization?**
   - It prevents the model from fitting noise in training data.

5. **What does patience in early stopping mean?**
   - Number of epochs to wait before stopping if no improvement.

6. **Can early stopping be used with any model?**
   - Yes, as long as validation metrics are monitored.

7. **What happens if patience is too small?**
   - Model may stop before reaching optimal performance.

8. **What is the tradeoff of L2 regularization?**
   - May slightly reduce training accuracy but improves generalization.

9. **How do you decide the regularization strength?**
   - Tune hyperparameters using validation sets or cross-validation.

10. **When to combine early stopping and L2?**
   - When dataset is prone to overfitting, combining both improves robustness.
