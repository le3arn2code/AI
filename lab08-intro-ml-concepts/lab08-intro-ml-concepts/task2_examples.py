# Task 2 – Example Code for Supervised and Unsupervised Learning

# Supervised Learning: Classification with k-NN
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# k-NN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predictions + accuracy
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Supervised Learning (k-NN Classification) Accuracy: {accuracy:.2f}")

# --------------------------------------------------------------

# Unsupervised Learning: Clustering with k-Means
import matplotlib
matplotlib.use("Agg")  # Safe backend for servers/headless
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate sample data
X_blobs, _ = make_blobs(n_samples=300, centers=4,
                        cluster_std=0.60, random_state=0)

# k-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
y_kmeans = kmeans.fit_predict(X_blobs)

# Save plot
plt.scatter(X_blobs[:, 0], X_blobs[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X')
plt.title('k-Means Clustering')
plt.savefig("kmeans_clusters.png")
print("✅ Unsupervised Learning (k-Means Clustering) plot saved as kmeans_clusters.png")
