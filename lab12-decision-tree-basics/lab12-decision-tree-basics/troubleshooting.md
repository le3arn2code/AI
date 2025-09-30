# Troubleshooting

1. **ModuleNotFoundError: No module named 'graphviz'**
   - Install Graphviz: `pip install graphviz --break-system-packages`
   - Install system package: `sudo apt install graphviz -y`

2. **PDF not opening after render**
   - Check that Graphviz is installed correctly. Open manually: `xdg-open iris_tree.pdf`.

3. **Accuracy seems too high**
   - The model is trained and tested on the same dataset here. For realistic evaluation, use train/test split.
