#!/usr/bin/env bash
set -euo pipefail

echo "🚀 Updating pip..."
python3 -m pip install --upgrade pip --break-system-packages

echo "📦 Installing requirements (gymnasium)..."
pip3 install -r requirements.txt --break-system-packages

echo "▶️ Running lab..."
python3 lab31_rl_intro.py
