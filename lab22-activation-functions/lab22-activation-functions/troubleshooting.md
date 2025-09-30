# Troubleshooting - Lab 22

- **ModuleNotFoundError**: Install missing packages with `pip install tensorflow scikit-learn numpy pandas matplotlib`.
- **TypeError: OneHotEncoder got unexpected argument 'sparse'**: Use `OneHotEncoder()` and then call `.toarray()` on the result.
- **Training too slow**: Reduce epochs or batch size.
- **CUDA errors**: Ignore if you're on CPU; TensorFlow will fall back to CPU automatically.
