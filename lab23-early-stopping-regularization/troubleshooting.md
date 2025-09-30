# Troubleshooting

## Common Issues

### 1. `ModuleNotFoundError: No module named 'tensorflow.python'`
- This happens if TensorFlow was installed incorrectly.
- Fix: reinstall TensorFlow properly:
```bash
pip uninstall keras tensorflow
pip install tensorflow==2.15 keras==2.15
```
Use `tensorflow.keras` instead of `keras` standalone.

### 2. CUDA/GPU Errors
- You may see warnings about missing CUDA drivers if running on CPU-only systems.
- Ignore them; TensorFlow will fall back to CPU.

