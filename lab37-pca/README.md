# Lab 37: Simple Dimensionality Reduction (PCA)

## Overview
This lab demonstrates **Principal Component Analysis (PCA)** for dimensionality reduction using the Iris dataset.  
PCA helps in reducing the number of features while retaining most of the variance, making models more efficient.

## Objectives
- Understand PCA concepts: variance, principal components.
- Standardize data before applying PCA.
- Apply PCA on the Iris dataset.
- Visualize explained variance ratio (scree plot).
- Use top 2 principal components for classification with Logistic Regression.
- Evaluate classification accuracy.

## Results
- Scree plot showed variance explained by each component.
- Logistic Regression classifier trained on the first 2 PCA components.
- **Final Accuracy:** ~0.91 (91.1%)

## Key Takeaways
- PCA reduces dimensionality while minimizing information loss.
- Choosing components based on explained variance ensures efficiency without much accuracy loss.
