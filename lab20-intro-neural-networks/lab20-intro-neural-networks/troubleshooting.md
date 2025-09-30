# Troubleshooting

- **ModuleNotFoundError: No module named 'networkx'**
  - Install networkx: `pip install networkx`

- **Matplotlib errors when saving figure**
  - Ensure matplotlib is installed: `pip install matplotlib`
  - Avoid using `plt.show()` on headless servers. Use `plt.savefig()` instead.

- **Numpy RuntimeWarning for exp overflow**
  - Happens with very large positive/negative numbers in sigmoid. Not harmful here.
