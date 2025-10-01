# Step 1: Create virtual environment
python3 -m venv lab38-venv
source lab38-venv/bin/activate

# Step 2: Install dependencies
pip install --upgrade pip
pip install flask streamlit scikit-learn numpy

# Step 3: Create and save model
python3 create_model.py

# Step 4: Run Flask app
python3 lab38_app.py

# Step 5: Test in CLI (new terminal)
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/predict-form
curl -X POST -F "input_data=5.1,3.5,1.4,0.2" http://127.0.0.1:5000/predict-form
