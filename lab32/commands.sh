#!/bin/bash
# Step 3 Lab 32 Commands

# Activate virtual environment
source ~/otel-auto-lab-venv/bin/activate

# Pre-flight checks
python3 --version
pip --version

# Install dependencies
pip install --upgrade pip
pip install numpy matplotlib tensorflow scikit-image pillow

# Run Task 2 (augmentation visualization)
python3 task2_augmentation.py

# Run Task 3 (no augmentation training)
python3 task3_no_augmentation.py

# Run Task 3 (with augmentation training)
python3 task3_with_augmentation.py
