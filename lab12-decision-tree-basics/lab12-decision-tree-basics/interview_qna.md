# Interview Q&A: Decision Trees

1. **Q: What is a decision tree?**
   - A: A supervised learning algorithm used for classification and regression tasks by splitting data into branches.

2. **Q: What criterion does scikit-learn’s DecisionTreeClassifier use by default?**
   - A: Gini impurity.

3. **Q: How do you prevent overfitting in decision trees?**
   - A: By pruning, setting max_depth, min_samples_split, or min_samples_leaf.

4. **Q: What are advantages of decision trees?**
   - A: Easy to interpret, handle categorical & numerical data, non-parametric.

5. **Q: What are disadvantages of decision trees?**
   - A: Prone to overfitting, unstable with small changes in data, biased towards features with many levels.

6. **Q: How are feature importances calculated?**
   - A: Based on the reduction in impurity (e.g., Gini or entropy) contributed by each feature.

7. **Q: What is the role of entropy in decision trees?**
   - A: It measures impurity; trees split to reduce entropy (information gain).

8. **Q: How do decision trees handle missing values?**
   - A: scikit-learn does not handle missing values natively; preprocessing is required.

9. **Q: What’s the difference between classification and regression trees?**
   - A: Classification predicts discrete labels; regression predicts continuous values.

10. **Q: When should you not use decision trees?**
   - A: With very high-dimensional sparse data (better suited for linear models).
