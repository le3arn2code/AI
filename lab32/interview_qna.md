# Lab 32: Data Augmentation - Interview Q&A

### 1. What is data augmentation?
It is a method to artificially increase dataset diversity by applying transformations like flips, rotations, zoom, and shifts.

### 2. Why is data augmentation important?
It prevents overfitting and helps models generalize better when training data is limited.

### 3. When should you use data augmentation?
When datasets are small or limited, especially for computer vision tasks like image classification and detection.

### 4. What are common augmentation techniques?
Rotation, flipping, zoom, cropping, shifting, brightness adjustment, and adding noise.

### 5. Which libraries support augmentation?
TensorFlow (`ImageDataGenerator`), PyTorch (`torchvision.transforms`), Pillow, and scikit-image.

### 6. What errors did you face in this lab?
- Missing PIL/scikit-image → installed with pip.  
- Externally managed environment → solved with venv.  
- Version mismatch (TensorFlow vs Pillow) → upgraded pip and reinstalled.  
- Missing `sample_image.jpg` → added manually.

### 7. How does augmentation affect performance?
It improves validation accuracy and reduces overfitting, making the model more robust.

### 8. Can augmentation replace real data?
No. Real diverse data is always preferable; augmentation is a supplement.

### 9. How did you implement augmentation here?
By using `ImageDataGenerator` with `rotation_range=40`, `horizontal_flip=True`, and `vertical_flip=True`.

### 10. What is the key takeaway?
Even simple augmentations like flipping and rotation significantly improve model performance with limited datasets.
