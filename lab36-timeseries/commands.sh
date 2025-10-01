# Step-by-step commands for Ubuntu 24.04

# 1. Update and install prerequisites
sudo apt update
sudo apt install -y python3-venv

# 2. Create and activate virtual environment
python3 -m venv ~/lab36-venv
source ~/lab36-venv/bin/activate

# 3. Upgrade pip
python3 -m pip install --upgrade pip

# 4. Install required libraries
pip install pandas numpy matplotlib statsmodels scikit-learn

# 5. Run the lab script
python3 lab36_timeseries.py
