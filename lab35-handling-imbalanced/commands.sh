# Commands to reproduce Lab 35: Handling Imbalanced Datasets

# Step 1: Update system and install venv
sudo apt update
sudo apt install -y python3-venv

# Step 2: Create and activate virtual environment
python3 -m venv ~/lab35-venv
source ~/lab35-venv/bin/activate

# Step 3: Upgrade pip
python3 -m pip install --upgrade pip

# Step 4: Install required libraries
pip install numpy pandas scikit-learn matplotlib imbalanced-learn

# Step 5: Verify installation
python3 -c "import numpy, pandas, sklearn, matplotlib, imblearn; print('✅ All libraries installed successfully')"

# Step 6: Run the Python script
python3 lab35_imbalanced.py
