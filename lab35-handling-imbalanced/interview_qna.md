# Interview Q&A: Handling Imbalanced Datasets

**Q1. What is an imbalanced dataset?**  
A dataset where one class occurs far more frequently than the other(s). Example: 990 non-fraud vs 10 fraud cases.

**Q2. Why are imbalanced datasets problematic?**  
Because models may predict only the majority class and still achieve high accuracy, but perform poorly on the minority class.

**Q3. What is SMOTE?**  
Synthetic Minority Over-sampling Technique. It creates synthetic examples of minority class by interpolating between existing samples.

**Q4. Difference between oversampling and undersampling?**  
Oversampling increases minority class samples (e.g., SMOTE).  
Undersampling reduces majority class samples. Both aim to balance class distribution.

**Q5. Why not just duplicate minority samples instead of SMOTE?**  
Duplication can lead to overfitting. SMOTE creates synthetic variations, improving generalization.

**Q6. What metrics are better than accuracy for imbalanced datasets?**  
Precision, Recall, F1-score, AUC-ROC. These focus on the minority class performance.

**Q7. What did the lab show before balancing?**  
Perfect accuracy/precision/recall, but misleading since only 4 fraud cases existed in test data.

**Q8. What changed after applying SMOTE?**  
Balanced dataset improved recall for fraud cases and gave more realistic performance metrics.

**Q9. Can SMOTE be harmful?**  
Yes. It may introduce noise if synthetic samples are unrealistic. Must be used carefully.

**Q10. What are alternatives to SMOTE?**  
ADASYN, Borderline-SMOTE, Random Undersampling, Ensemble methods like BalancedBaggingClassifier, or cost-sensitive learning.
