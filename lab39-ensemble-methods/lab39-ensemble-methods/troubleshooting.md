# Troubleshooting Notes

1. **LF/CRLF warnings**  
   Git warned about LF to CRLF conversion. This does not affect code execution.  
   ✅ Fix: Configure `.gitattributes` or accept the auto-conversion.

2. **Dependency mismatches**  
   Some labs raised version issues with numpy/scipy.  
   ✅ Fix: Reinstall with `pip3 install --upgrade` and `--break-system-packages`.

3. **Repeated runs in Alnafi cloud**  
   Commands sometimes run twice. This is due to the environment setup.  
   ✅ Workaround: Ignore the duplicate execution since results remain valid.

