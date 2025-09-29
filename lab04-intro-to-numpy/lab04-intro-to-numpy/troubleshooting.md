# Troubleshooting

## Issue: Cannot install numpy with pip3 (externally managed environment)
**Error:**
```
error: externally-managed-environment
```
**Solution:**
Install numpy using apt:
```
sudo apt install python3-numpy -y
```

## Issue: ImportError for numpy
Make sure numpy is installed and Python3 is used:
```
python3 -m pip show numpy
```
