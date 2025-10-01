# Troubleshooting Log - Lab 34

## Issue 1: SHAP API mismatch
- **Error:** 
  ```
  TypeError: In v0.20, force plot now requires the base value as the first parameter!
  ```
- **Cause:** SHAP v0.48.0 was installed by default.
- **Resolution:** Downgraded to SHAP 0.39.0 for compatibility.
  ```bash
  pip install shap==0.39.0
  ```

## Issue 2: System reboot
- **Error:** `Broadcast message from root... system will power off`
- **Cause:** AWS EC2 instance auto-shutdown.
- **Resolution:** Reconnected via SSH and re-activated virtual environment.

## Issue 3: Package installation mismatches
- Initially installed SHAP 0.48.0, which was incompatible.
- Solution: Explicitly pin dependencies in `commands.sh`.

---
All issues resolved. Final lab ran successfully with correct SHAP visualizations.
