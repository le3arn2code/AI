# Troubleshooting for Lab 24

1. **ModuleNotFoundError: No module named 'keras'**
   - Install keras and tensorflow with:
     ```bash
     pip install keras tensorflow
     ```

2. **Matplotlib not found**
   - Install matplotlib:
     ```bash
     pip install matplotlib
     ```

3. **Training very slow**
   - Running on CPU is expected if GPU drivers are missing. This is fine for MNIST.

4. **MemoryError**
   - Reduce batch size in training from 64 to 32.
