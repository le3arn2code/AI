#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Updating pip..."
python3 -m pip install --upgrade pip --break-system-packages

echo "📦 Installing requirements (scikit-learn, pandas)..."
pip3 install -r requirements.txt --break-system-packages

echo "▶️ Running the lab script..."
python3 lab29_vectorization.py
