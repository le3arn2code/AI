# Troubleshooting Guide for Lab 15

1. **ModuleNotFoundError: No module named 'sklearn'**
   - Fix: Install scikit-learn using `pip install --break-system-packages scikit-learn`.

2. **ModuleNotFoundError: No module named 'matplotlib'**
   - Fix: Install matplotlib with `pip install --break-system-packages matplotlib`.

3. **Decision Tree accuracy too low**
   - Ensure dataset is correctly split and max_depth is varied.

4. **Empty plot generated**
   - Make sure `plt.savefig("depth_vs_performance.png")` is present before `plt.show()`.

5. **Different accuracy each run**
   - Use `random_state=42` for reproducibility.
