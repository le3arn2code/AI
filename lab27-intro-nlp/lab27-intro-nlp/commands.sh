#!/usr/bin/env bash
set -euo pipefail
python3 -m pip install --upgrade pip --break-system-packages
pip3 install -r requirements.txt --break-system-packages
python3 scripts/run_all.py
