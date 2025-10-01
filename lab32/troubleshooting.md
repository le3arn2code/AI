# Troubleshooting - Lab 32

## Errors Encountered
1. **Software mismatch**
   - Issue: Missing or wrong versions of TensorFlow, Matplotlib, or Pillow.
   - Fix: Installed correct versions with pip.

2. **Folder conflicts in Git**
   - Issue: Duplicate folders caused Git reset errors on Windows.
   - Fix: Manually removed using `rm -rf` and reset to `origin/main`.

3. **Rebase errors**
   - Issue: Repo stuck in `REBASE` state.
   - Fix: Aborted rebase and deleted `.git/rebase-merge` manually, then reset branch.
