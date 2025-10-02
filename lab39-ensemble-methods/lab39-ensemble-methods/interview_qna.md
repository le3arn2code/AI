# Lab 39: Interview Q&A

1. **Q: What is Bagging in ML?**  
   A: Bagging (Bootstrap Aggregating) trains multiple models on bootstrapped datasets and combines their results to reduce variance.

2. **Q: How does Random Forest improve over a Decision Tree?**  
   A: Random Forest reduces overfitting by averaging multiple trees built on random subsets of features and data.

3. **Q: What is Boosting?**  
   A: Boosting trains models sequentially where each model corrects the errors of the previous, reducing bias.

4. **Q: Difference between Bagging and Boosting?**  
   A: Bagging reduces variance (parallel independent models). Boosting reduces bias (sequential dependent models).

5. **Q: When should you use Random Forest?**  
   A: When you need robust, quick-to-train models with reduced variance and good generalization.

6. **Q: When is Gradient Boosting preferable?**  
   A: When accuracy is critical, and computational cost is acceptable, as boosting often yields better performance.

7. **Q: What are common issues with Gradient Boosting?**  
   A: It can overfit on noisy data and is computationally more expensive.

8. **Q: How do ensemble methods improve model generalization?**  
   A: By combining multiple models, they average out individual model errors.

9. **Q: Can Bagging and Boosting be combined?**  
   A: Yes, methods like Stacking or advanced frameworks (XGBoost, LightGBM) combine both ideas.

10. **Q: How do you handle CRLF vs LF in code repos?**  
    A: Configure `.gitattributes` to enforce consistency or rely on Git auto-conversion.
