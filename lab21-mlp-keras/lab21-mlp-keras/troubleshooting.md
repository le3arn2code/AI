# Troubleshooting

1. **CUDA/GPU Errors**
   - If you see CUDA errors, TensorFlow is falling back to CPU. This is fine for MNIST.

2. **HDF5 Save Warning**
   - Use `.keras` format instead of legacy `.h5`.

3. **Memory Issues**
   - Ensure enough RAM is available; MNIST is lightweight so should be fine.

4. **Convergence Issues**
   - Increase epochs or hidden layer size if accuracy is low.
