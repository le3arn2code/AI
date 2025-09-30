results_table = """
Activation Function   Test Accuracy   Observations
--------------------------------------------------
Sigmoid               ~0.93           Good for binary, struggles with deeper networks
Tanh                  ~0.96           Performs better than Sigmoid
ReLU                  ~0.98           Fast convergence, avoids vanishing gradients
Leaky ReLU            ~0.97           Solves dying ReLU problem
"""

print(results_table)
