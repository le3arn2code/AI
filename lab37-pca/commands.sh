#!/bin/bash
# Step 1: Update system and install Python venv
sudo apt update
sudo apt install -y python3-venv

# Step 2: Create and activate virtual environment
python3 -m venv ~/lab37-venv
source ~/lab37-venv/bin/activate

# Step 3: Upgrade pip
python3 -m pip install --upgrade pip

# Step 4: Install required libraries
pip install numpy pandas matplotlib scikit-learn

# Step 5: Run the lab script
python3 lab37_pca.py
