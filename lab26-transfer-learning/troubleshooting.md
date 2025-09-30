# Troubleshooting Guide for Lab 26: Transfer Learning

### 1. CUDA / GPU Errors
- If you see warnings like:
  ```
  Could not find cuda drivers on your machine, GPU will not be used.
  ```
  → This is safe to ignore if you are running on CPU. Training will just be slower.

### 2. ValueError: Unknown variable in optimizer
- Cause: Loading a model with optimizer state mismatches the current session.
- Fix: Always reload with `compile=False` and recompile with fresh optimizer.

### 3. Dataset Not Found
- Error:
  ```
  FileNotFoundError: [Errno 2] No such file or directory: '/home/toor/datasets/cats_and_dogs_filtered/train'
  ```
- Fix: Ensure dataset is downloaded and placed under the correct path:
  ```
  /home/toor/datasets/cats_and_dogs_filtered/train/cats/
  /home/toor/datasets/cats_and_dogs_filtered/train/dogs/
  ```

### 4. Plot not showing
- Since scripts run headless, the plot is saved as:
  ```
  transfer_learning_training.png
  ```
