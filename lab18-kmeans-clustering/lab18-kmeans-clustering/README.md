# Lab 18: Intro to Clustering (K-Means)

## Objectives
- Understand clustering fundamentals and its importance.
- Implement K-Means clustering using scikit-learn.
- Visualize and interpret resulting clusters.

## Lab Tasks
1. **Generate Dataset**
   - Create synthetic dataset with `make_blobs`.
   - Save visualization to `dataset.png`.

2. **Apply K-Means**
   - Use Elbow Method to decide `k`.
   - Save elbow plot to `elbow_method.png`.
   - Save cluster labels in `cluster_labels.txt`.

3. **Visualize Clusters**
   - Plot clusters with different colors.
   - Save final cluster visualization to `clusters.png`.

## How to Run
```bash
python3 task1_generate_dataset.py
python3 task2_kmeans.py
python3 task3_visualize_clusters.py
```

Outputs: `dataset.png`, `elbow_method.png`, `clusters.png`, and `cluster_labels.txt`.
