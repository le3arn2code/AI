# Troubleshooting - Lab 32: Data Augmentation

## Issue 1: Externally Managed Environment
**Error:** 
```
error: externally-managed-environment
```
**Fix:**  
Activated a virtual environment (`~/otel-auto-lab-venv`) and installed packages there.

---

## Issue 2: Missing Libraries
**Error:** 
```
ModuleNotFoundError: No module named 'PIL'
```
**Fix:**  
Installed missing libraries:
```
pip install pillow scikit-image
```

---

## Issue 3: Missing Sample Image
**Error:** 
```
FileNotFoundError: [Errno 2] No such file or directory: 'sample_image.jpg'
```
**Fix:**  
Placed an image named `sample_image.jpg` in the working directory.

---

## Issue 4: Software Version Mismatch
**Problem:** TensorFlow required specific versions of Pillow and NumPy.  
**Fix:** Upgraded pip and reinstalled libraries to ensure compatibility:
```
pip install --upgrade pip
pip install numpy pillow
```
