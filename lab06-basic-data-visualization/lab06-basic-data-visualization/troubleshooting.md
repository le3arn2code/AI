# Troubleshooting

- **ModuleNotFoundError: No module named 'matplotlib'**
  ```bash
  pip3 install matplotlib --break-system-packages
  ```

- **ModuleNotFoundError: No module named 'numpy'**
  ```bash
  pip3 install numpy --break-system-packages
  ```

- **No plot appears**
  - Ensure you are saving with `plt.savefig()` (done in this lab).
  - If running interactively, avoid `plt.show()` in headless environments.
