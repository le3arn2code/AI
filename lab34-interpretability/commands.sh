#!/bin/bash
# Lab 34: Intro to Model Interpretability

# Step 1: Create virtual environment
python3 -m venv ~/otel-auto-lab-venv

# Step 2: Activate virtual environment
source ~/otel-auto-lab-venv/bin/activate

# Step 3: Upgrade pip
python3 -m pip install --upgrade pip

# Step 4: Install required libraries (compatible versions)
pip install pandas numpy scikit-learn matplotlib ipython shap==0.39.0

# Step 5: Run the lab script
python3 lab34_interpretability.py
