# Lab 32: Data Augmentation (Concept)

This lab demonstrated the concept and benefits of **data augmentation** in machine learning.  
We applied basic transformations such as flipping and rotation on sample images using TensorFlow’s `ImageDataGenerator`.  

We then trained a simple CNN on CIFAR-10 both **without augmentation** and **with augmentation**, comparing validation accuracy and loss to assess improvements.  

## Errors and Fixes
- **Externally Managed Environment** → solved by using a Python virtual environment (`~/otel-auto-lab-venv`).  
- **Missing Libraries (PIL, scikit-image)** → installed with `pip install pillow scikit-image`.  
- **Software Version Mismatch** → fixed by upgrading pip and reinstalling TensorFlow dependencies.  
- **Sample Image Not Found** → resolved by placing `sample_image.jpg` in the working directory.  

## Conclusion
Data augmentation improves model **generalization** by exposing it to diverse variations of training data.  
Even simple transformations like flips and rotations showed improved validation performance compared to models trained without augmentation.
