# Lab 26: Basic Transfer Learning with VGG16

This lab demonstrates how to use transfer learning with the VGG16 model in Keras.  
You will load a pre-trained VGG16, add custom layers, and train on a cats vs. dogs dataset.

## Steps
1. **Task 1:** Load VGG16 base model and freeze layers.
2. **Task 2:** Add custom layers and save full model.
3. **Task 3:** Train model on dataset and save training plot.

## Dataset
Expected dataset path:
```
/home/toor/datasets/cats_and_dogs_filtered/train/
    cats/
    dogs/
```

## Run
```bash
python3 task1_load_vgg16.py
python3 task2_add_custom_layers.py
python3 task3_train_transfer_learning.py
```
