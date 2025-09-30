# Troubleshooting - Lab 18

1. **ModuleNotFoundError**
   - Ensure required libraries are installed:
     ```bash
     pip install numpy matplotlib scikit-learn --break-system-packages
     ```

2. **ConvergenceWarning**
   - Sometimes KMeans does not converge for higher clusters.
   - Use `n_init=10` or higher in `KMeans`.

3. **Plot not showing**
   - We save plots as `.png` files instead of using `plt.show()` for cloud/VM environments.

4. **FileNotFoundError**
   - Ensure you are in the correct directory before running scripts.
