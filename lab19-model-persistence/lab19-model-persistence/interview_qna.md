# Interview Q&A on Model Persistence

1. **Why is model persistence important?**
   - It saves time by avoiding retraining models every time.

2. **Which libraries are commonly used for persistence in Python?**
   - joblib and pickle.

3. **Why use joblib over pickle?**
   - Joblib is optimized for large numpy arrays, common in ML models.

4. **Can persisted models be used across Python versions?**
   - Not always; compatibility may break between versions.

5. **What is the risk of using pickle for persistence?**
   - Pickle can execute arbitrary code during loading (security risk).

6. **How do you share a trained model with others?**
   - Save it with joblib/pickle and share the file.

7. **Can you persist models in cloud platforms?**
   - Yes, store them in S3, GCS, or Azure Blob storage.

8. **What is the format of a joblib-saved file?**
   - A `.joblib` binary file.

9. **How do you check if the loaded model works?**
   - Run `.predict()` on test data.

10. **When should you retrain instead of reusing a saved model?**
   - When data distribution changes (concept drift).