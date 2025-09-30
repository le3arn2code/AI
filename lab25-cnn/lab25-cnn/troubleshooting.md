# Troubleshooting for Lab 25

## Common Issues

### 1. GPU Not Found
Error: `Could not find cuda drivers...`
- Cause: No GPU installed or CUDA not set up.
- Fix: Training will still work on CPU. Ignore this warning.

### 2. HDF5 Save Warning
Warning: `You are saving your model as an HDF5 file...`
- Fix: Use `.keras` format instead of `.h5`, or ignore since `.h5` works fine.

### 3. Memory Allocation Warnings
Error: `Allocation exceeds 10% of free system memory`
- Fix: Reduce batch size (e.g., from 64 to 32).

