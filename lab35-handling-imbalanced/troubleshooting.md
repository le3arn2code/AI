# Troubleshooting Notes

## Issue 1: Repository GPG key errors and Hash Sum mismatch
- During `apt update`, errors appeared due to expired/invalid repo keys and hash mismatches for Google Chrome & Puppet repos.
- Resolution: Ignored non-essential repos (e.g., Jenkins, Puppet, Chrome). Core Ubuntu repos worked fine, allowing Python packages to be installed.

## Issue 2: SHAP-related force plot errors (from earlier labs)
- SHAP's `force_plot` API changed in v0.20 requiring a `base_value` argument.
- Resolution: Adjusted code accordingly (though not part of this lab, noted for continuity).

## Issue 3: Pip upgrade mismatch
- Initially pip 24.0 was installed, upgraded cleanly to pip 25.2.

## Outcome:
All necessary Python libraries (numpy, pandas, scikit-learn, matplotlib, imbalanced-learn) were successfully installed, and the lab executed with correct outputs.
