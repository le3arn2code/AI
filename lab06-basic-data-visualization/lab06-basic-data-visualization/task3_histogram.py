import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.randn(1000)

plt.hist(data, bins=30, color='green', alpha=0.7)
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.savefig("histogram.png")
plt.close()
