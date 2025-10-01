# Lab 34: Intro to Model Interpretability

## Overview
This lab introduces **Model Interpretability** using SHAP (SHapley Additive exPlanations) on the Iris dataset with a Random Forest classifier.  
The goal is to understand how features contribute to predictions and why interpretability is crucial for **trust, debugging, and compliance** in AI.

## Layman's Explanation
Think of a machine learning model like a **black box** that makes predictions. Interpretability is about opening that box to **see why** a model made a decision.  
In this lab, we used SHAP to break down predictions into contributions from each feature. For example, if the model predicts a flower is *Iris-setosa*, SHAP shows whether features like *petal length* or *sepal width* pushed that decision up or down.

This is important because:
- It builds **trust** (we know why the model predicted something).
- It helps with **debugging** (we can see if the model relies on wrong signals).
- It supports **compliance** (explanations are required in regulated industries).

## Steps in the Lab
1. Set up Python virtual environment and install required libraries.
2. Train a **Random Forest Classifier** on the Iris dataset.
3. Use **SHAP Explainer** to compute feature contributions.
4. Visualize model explanations with SHAP plots.

## Issues Faced & Solutions
- **SHAP API mismatch**: The lab instructions were written for older SHAP (0.39), but the VM had SHAP (0.48).  
  - Error: `TypeError: In v0.20, force plot now requires the base value...`  
  - Solution: Pin SHAP version to 0.39.0 (`pip install shap==0.39.0`).  
  - This restored compatibility with lab instructions without modifying code.
- **System reboot during lab**: AWS EC2 auto-shutdown caused a disconnect.  
  - Solution: Reconnected to instance and re-activated virtual environment.

## Final Outcome
- A Random Forest model was trained successfully.
- SHAP was applied to explain individual predictions and overall feature importance.
- Interpretability was demonstrated clearly with feature contribution plots.

---
