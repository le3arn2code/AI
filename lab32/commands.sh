#!/bin/bash
# Commands for Lab 32: Data Augmentation

# 1. Activate virtual environment
source ~/otel-auto-lab-venv/bin/activate

# 2. Install dependencies
pip install numpy matplotlib tensorflow pillow --break-system-packages

# 3. Run the augmentation code
python3 lab32_augmentation.py
