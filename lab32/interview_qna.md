# Interview Q&A - Lab 32: Data Augmentation

1. **What is data augmentation?**
   - A technique to artificially increase training data diversity using transformations like flipping and rotation.

2. **Why is data augmentation important?**
   - It prevents overfitting and improves model generalization.

3. **When should you use data augmentation?**
   - When the dataset is small or lacks variety.

4. **Give examples of augmentation techniques.**
   - Flipping, rotation, scaling, cropping, color jitter, noise injection.

5. **How does augmentation improve performance?**
   - It exposes the model to varied versions of the data, making it robust to real-world variations.

6. **Can augmentation replace collecting real data?**
   - No, but it complements small datasets effectively.

7. **What’s the difference between offline and online augmentation?**
   - Offline: Preprocess dataset and save augmented copies.
   - Online: Apply augmentations on the fly during training.

8. **What libraries support augmentation in Python?**
   - TensorFlow/Keras (`ImageDataGenerator`), PyTorch (`torchvision.transforms`), Albumentations.

9. **What happens if you over-augment data?**
   - It can distort images too much, leading to poor learning.

10. **How would you explain data augmentation to a non-technical person?**
   - Like showing a child a toy from different angles so they learn to recognize it in any position.
