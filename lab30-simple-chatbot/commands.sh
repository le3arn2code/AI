#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Updating pip..."
python3 -m pip install --upgrade pip --break-system-packages

echo "📦 Installing requirements (none external) ..."
pip3 install -r requirements.txt --break-system-packages

echo "▶️ Running chatbot ..."
python simple_chatbot.py
