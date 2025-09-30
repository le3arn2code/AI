import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Generate dataset
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualize dataset
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Sample Dataset Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.savefig("dataset.png")
print("✅ Dataset plot saved as dataset.png")
