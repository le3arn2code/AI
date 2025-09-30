# Interview Q&A: Overfitting vs. Underfitting

1. **What is overfitting in ML?**
   - When a model learns noise in training data and performs poorly on unseen data.

2. **What is underfitting?**
   - When a model is too simple to capture the underlying trend in the data.

3. **How can you detect overfitting?**
   - High training accuracy but low validation/test accuracy.

4. **How can you detect underfitting?**
   - Both training and validation accuracies are low.

5. **What techniques can prevent overfitting?**
   - Cross-validation, pruning decision trees, regularization, dropout in neural networks.

6. **What role does model complexity play?**
   - High complexity → risk of overfitting; Low complexity → risk of underfitting.

7. **What is the bias-variance tradeoff?**
   - Bias = error due to simplicity, Variance = error due to complexity. Goal is balance.

8. **Can increasing data reduce overfitting?**
   - Yes, more data can help the model generalize better.

9. **Why do we use validation sets?**
   - To evaluate model performance on unseen data and detect over/underfitting.

10. **Give a real-life example of overfitting.**
   - Predicting housing prices where the model memorizes rare outliers instead of general trends.
