import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ReLU function
def relu(x):
    return np.maximum(0, x)

# Test
inputs = np.array([-2, -1, 0, 1, 2])
print("Inputs:", inputs)
print("Sigmoid outputs:", sigmoid(inputs))
print("ReLU outputs:", relu(inputs))
