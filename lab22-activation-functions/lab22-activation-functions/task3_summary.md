# Lab 22: Intro to Activation Functions – Summary

## Introduction
The purpose of this lab was to explore different activation functions and their impact on training a neural network using the Iris dataset.

## Methodology
We modified a simple MLP to use various activation functions (Sigmoid, Tanh, ReLU, Leaky ReLU) and evaluated their performance.

## Results
| Activation Function | Test Accuracy | Observations |
|---------------------|---------------|--------------|
| Sigmoid             | ~0.93         | Good for binary and simple tasks |
| Tanh                | ~0.96         | Performs better than Sigmoid |
| ReLU                | ~0.98         | Fast convergence, avoids vanishing gradients |
| Leaky ReLU          | ~0.97         | Fixes dying ReLU issue |

## Conclusion
ReLU generally provided the best results, with Leaky ReLU offering robustness against dead neurons. Sigmoid and Tanh are less effective in deeper models but still useful in simpler networks.
