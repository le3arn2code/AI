#!/bin/bash
python3 -m pip install --upgrade pip --break-system-packages
pip install numpy pandas scikit-learn --break-system-packages
python3 lab33_gridsearch.py
