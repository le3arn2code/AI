# Interview Q&A - Clustering (K-Means)

1. **Q:** What is K-Means clustering?  
   **A:** An unsupervised algorithm that partitions data into `k` clusters by minimizing intra-cluster distances.

2. **Q:** How is the number of clusters `k` chosen?  
   **A:** Often determined using the Elbow Method, Silhouette score, or domain knowledge.

3. **Q:** What are the limitations of K-Means?  
   **A:** Requires specifying `k`, sensitive to initialization, assumes spherical clusters.

4. **Q:** What metric does K-Means optimize?  
   **A:** Inertia (sum of squared distances to the nearest centroid).

5. **Q:** What initialization method is commonly used in K-Means?  
   **A:** K-Means++ for better centroid initialization.

6. **Q:** How does scaling affect K-Means?  
   **A:** Features should be scaled, as K-Means relies on distance measures.

7. **Q:** What happens if clusters are not spherical?  
   **A:** K-Means may misclassify; other methods like DBSCAN or GMM may work better.

8. **Q:** Is K-Means deterministic?  
   **A:** No, results vary with initialization unless random_state is fixed.

9. **Q:** When is K-Means useful in business?  
   **A:** Customer segmentation, market analysis, anomaly detection.

10. **Q:** How do you evaluate K-Means clusters?  
   **A:** Using metrics like Silhouette Score, Davies-Bouldin index, or visual inspection.
