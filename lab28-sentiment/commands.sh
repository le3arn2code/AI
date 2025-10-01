#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Updating pip..."
python3 -m pip install --upgrade pip --break-system-packages

echo "📦 Installing requirements (pandas, scikit-learn, nltk)..."
pip3 install -r requirements.txt --break-system-packages

echo "▶️ Running the lab script (expects IMDB Dataset.csv here)..."
python3 lab28_sentiment.py
