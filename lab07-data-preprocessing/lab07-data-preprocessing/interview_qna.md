# Interview Q&A – Data Preprocessing (10 Questions)

**Q1:** Why is data preprocessing important?  
**A1:** It ensures raw data is cleaned and transformed into a suitable format for analysis and modeling.

**Q2:** What are common methods for handling missing data?  
**A2:** Dropping rows/columns, filling with mean/median/mode, or using advanced imputation methods.

**Q3:** What is normalization and why is it used?  
**A3:** Normalization scales features to a common range, improving performance of algorithms like k-NN and gradient descent.

**Q4:** What’s the difference between normalization and standardization?  
**A4:** Normalization scales data to [0,1], while standardization centers data to mean 0 and variance 1.

**Q5:** Why is Min-Max scaling sensitive to outliers?  
**A5:** Because outliers distort the minimum and maximum values, shrinking normal data into a small range.

**Q6:** What is one-hot encoding?  
**A6:** It converts categorical variables into binary columns for each category.

**Q7:** What problem can arise with one-hot encoding?  
**A7:** It can create high-dimensional data if categorical columns have many unique values (curse of dimensionality).

**Q8:** What alternatives exist to one-hot encoding?  
**A8:** Label encoding, target encoding, or embedding representations.

**Q9:** Why is handling missing values critical before training ML models?  
**A9:** Many ML algorithms cannot handle NaN values and may produce errors or biased models.

**Q10:** How do you decide between dropping and filling missing data?  
**A10:** If missing data is small and random → drop. If significant or structured → fill with statistical/ML-based imputation.

