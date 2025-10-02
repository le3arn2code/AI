#!/bin/bash
# Commands for Lab 40: Final Project

# Step 1: Prepare dataset
mkdir -p ~/datasets && cd ~/datasets
kaggle datasets download -d camnugent/california-housing-prices
unzip california-housing-prices.zip -d california_housing

# Step 2: Run script
python3 lab40_final_project.py
