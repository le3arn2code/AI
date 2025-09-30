# Troubleshooting - Lab 13

1. **ModuleNotFoundError: No module named 'sklearn'**
   - Install scikit-learn: `pip install scikit-learn --break-system-packages`

2. **Confusion matrix not displaying**
   - Ensure you have matplotlib installed and running in GUI-capable environment.

3. **Low accuracy**
   - Try adjusting model parameters or use more training data.

4. **Blank plot**
   - Add `plt.show()` at the end of plotting code.
