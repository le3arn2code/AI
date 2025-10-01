# Lab 32: Data Augmentation

## 📝 Layman’s Explanation
Imagine teaching a child to recognize animals 🐶🐱. If you only show a few pictures of a cat always sitting the same way, the child may not recognize a cat lying down or upside down.  

**Data Augmentation** solves this problem by flipping, rotating, and transforming the same images in different ways. This way, the machine learning model sees many variations and learns to generalize better.  

In short: we artificially make our dataset **bigger and more diverse** without collecting new images, which helps prevent overfitting and improves performance on new data.

---

## 🎯 Objectives
- Understand the importance and benefits of data augmentation in ML.
- Learn basic augmentation techniques (flipping, rotation).
- Compare model performance with and without augmentation.

---

## 📦 Prerequisites
- Basic ML/DL concepts.
- Python basics.
- Familiarity with NumPy, Matplotlib, and TensorFlow/Keras.

---

## 🔧 Tools and Libraries
- Python 3.x  
- NumPy  
- Matplotlib  
- TensorFlow / Keras  
- PIL (for image handling)  

---

## 🛠️ Lab Tasks

### Task 1: Understanding Data Augmentation
- Why it is important.  
- When to use it.  

### Task 2: Applying Basic Augmentation
1. Load a sample image.  
2. Apply **rotation** and **flipping**.  
3. Show augmented images.  

### Task 3: Model Performance Comparison
1. Train model **without augmentation**.  
2. Train model **with augmentation**.  
3. Compare metrics (accuracy, loss).  

---

## ⚠️ Issues Faced & Fixes
- **Software mismatch** → Fixed by installing correct versions (`tensorflow`, `matplotlib`, `PIL`).  
- **Folder conflicts in Git** → Cleaned using `rm -rf` and hard reset.  
- **Rebase errors** → Resolved by aborting rebase and resetting to `origin/main`.  

---

## ✅ Conclusion
- Data augmentation is a simple yet powerful way to improve generalization.  
- Even basic techniques (flip, rotate) significantly help when data is limited.  
- Comparing results clearly shows improvement in validation accuracy when using augmentation.  

---

## 📂 Contents
- `lab32_augmentation.py` → main lab code.  
- `commands.sh` → command sequence for environment setup and running.  
- `troubleshooting.md` → errors faced and resolutions.  
- `interview_qna.md` → 10 interview Q&A on data augmentation.  
- Figures (`figure0.png`, `figure1.png`, etc.) → augmentation outputs.  
