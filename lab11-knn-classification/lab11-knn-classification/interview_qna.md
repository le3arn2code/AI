# Interview Q&A: KNN Classification

1. **Q: What is KNN?**
   - A: A non-parametric algorithm that classifies data based on the majority label of k nearest neighbors.

2. **Q: How do you choose k in KNN?**
   - A: Typically via cross-validation; small k may overfit, large k may underfit.

3. **Q: What distance metrics are used in KNN?**
   - A: Euclidean, Manhattan, Minkowski, Hamming (for categorical).

4. **Q: Is KNN sensitive to feature scaling?**
   - A: Yes, features must be normalized or standardized.

5. **Q: What is the computational cost of KNN?**
   - A: High during prediction (O(n)) since all distances must be computed.

6. **Q: Can KNN handle multiclass problems?**
   - A: Yes, by majority voting across neighbors.

7. **Q: What are advantages of KNN?**
   - A: Simple, no training time, works well with small datasets.

8. **Q: What are disadvantages of KNN?**
   - A: Slow prediction, sensitive to noise and irrelevant features.

9. **Q: How do you improve KNN performance?**
   - A: Use dimensionality reduction, feature selection, or KD-Trees/Ball Trees.

10. **Q: When should you avoid KNN?**
   - A: With large, high-dimensional datasets due to slow predictions and curse of dimensionality.
