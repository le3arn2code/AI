# Interview Q&A - Lab 34

### 1. What is model interpretability and why is it important?
**Answer:** Model interpretability means understanding how and why a model makes predictions. It builds trust, helps in debugging, and ensures compliance in regulated industries.

### 2. What is SHAP and how does it work?
**Answer:** SHAP (SHapley Additive exPlanations) assigns each feature a contribution value for a prediction, based on game theory’s Shapley values.

### 3. What is LIME and how is it different from SHAP?
**Answer:** LIME (Local Interpretable Model-agnostic Explanations) approximates the model locally with a simpler model, while SHAP gives globally consistent additive explanations.

### 4. Why did we use the Iris dataset in this lab?
**Answer:** The Iris dataset is small, well-known, and ideal for demonstrating interpretability without heavy computation.

### 5. What type of model was trained in this lab?
**Answer:** A Random Forest Classifier (ensemble of decision trees).

### 6. What issue did we face with SHAP in this lab?
**Answer:** SHAP v0.48 API mismatch with lab instructions, causing a TypeError in `force_plot`.

### 7. How was the SHAP mismatch resolved?
**Answer:** By downgrading to SHAP v0.39.0, which supports the lab’s original syntax.

### 8. What is the difference between global and local interpretability?
**Answer:** Global interpretability explains feature importance across the dataset, while local interpretability explains a single prediction.

### 9. Why is interpretability crucial in AI for healthcare or finance?
**Answer:** Because decisions affect human lives or financial outcomes, explanations are needed for accountability and compliance.

### 10. How would you explain SHAP to a non-technical stakeholder?
**Answer:** SHAP tells us how much each factor (like “petal length”) pushes a prediction up or down, similar to explaining how ingredients affect the taste of a dish.

---
