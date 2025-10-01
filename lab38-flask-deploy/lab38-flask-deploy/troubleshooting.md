# Troubleshooting Notes

## Issue 1: Flask server not reachable
- **Error:** `curl: (7) Failed to connect to 127.0.0.1 port 5000`
- **Fix:** Start Flask using `python3 lab38_app.py`.

## Issue 2: Missing dependencies
- **Error:** `ModuleNotFoundError`
- **Fix:** Ensure all dependencies installed:
  ```bash
  pip install flask streamlit scikit-learn numpy
  ```

## Issue 3: Wrong data format
- **Error:** ValueError when posting raw text.
- **Fix:** Ensure input format is comma-separated numbers (e.g., `5.1,3.5,1.4,0.2`).
