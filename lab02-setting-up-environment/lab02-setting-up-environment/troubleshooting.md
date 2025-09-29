# Troubleshooting - Lab 02

1. **Command not found: python3**
   - Install Python from https://www.python.org/downloads/

2. **pip not recognized**
   - Ensure Python is installed with "Add to PATH" checked.
   - Alternatively, use: `python3 -m ensurepip --upgrade`

3. **Permission denied during pip install**
   - Use virtual environments or run with `--user` flag.

4. **ModuleNotFoundError: No module named 'numpy'**
   - Reinstall using `pip install numpy` inside the virtual environment.

5. **Still issues?**
   - Restart your terminal and activate the virtual environment again.
