#!/bin/bash
# Step 3: Git push script for Lab 32 - Data Augmentation

# Unzip package into repo
unzip ../lab32-data-augmentation-fixed.zip -d lab32-data-augmentation

# Move into repo root (adjust path if needed)
cd ..

# Stage files
git add .

# Commit with message
git commit -m "Added Lab 32: Data Augmentation"

# Tag this commit
git tag lab32

# Push code and tag to GitHub
git push origin main
git push origin lab32
