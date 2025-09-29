#!/bin/bash
# Lab 02: Setting Up Your AI Environment

# Create virtual environment
python3 -m venv ai-lab-venv
source ai-lab-venv/bin/activate

# Install libraries
pip install numpy pandas scikit-learn

# Run tests
python3 test_numpy.py
python3 test_pandas.py
python3 test_sklearn.py

# Deactivate environment
deactivate
