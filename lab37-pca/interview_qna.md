# Interview Q&A - PCA and Dimensionality Reduction

**Q1: What is PCA and why is it used?**  
A: PCA (Principal Component Analysis) is a dimensionality reduction technique that transforms correlated features into orthogonal components, capturing maximum variance.

**Q2: Why do we standardize data before PCA?**  
A: PCA is sensitive to scale; standardization ensures all features contribute equally.

**Q3: What does explained variance ratio mean?**  
A: It shows how much variance each principal component captures relative to the dataset.

**Q4: How do you decide how many principal components to keep?**  
A: By examining the scree plot and cumulative explained variance (e.g., keep enough components to explain ~95% variance).

**Q5: Can PCA improve model accuracy?**  
A: Not always. It mainly improves efficiency and reduces overfitting, but accuracy can remain similar or slightly change.

**Q6: What are some limitations of PCA?**  
A: PCA is linear, may lose interpretability, and may not capture non-linear relationships.

**Q7: What is the difference between PCA and Feature Selection?**  
A: PCA creates new features (linear combinations), while feature selection chooses a subset of existing features.

**Q8: Can PCA be applied to categorical data?**  
A: No, PCA works on numerical continuous data.

**Q9: How is PCA different from LDA (Linear Discriminant Analysis)?**  
A: PCA is unsupervised (maximizes variance), LDA is supervised (maximizes class separation).

**Q10: In this lab, what accuracy did Logistic Regression achieve after PCA?**  
A: About **91.1%** accuracy using the first two principal components.
