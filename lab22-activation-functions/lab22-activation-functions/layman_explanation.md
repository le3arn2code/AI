# Layman Explanation of Lab 22

This lab tested different "switches" (activation functions) inside a neural network.

- Think of neurons as light bulbs that turn on differently depending on the switch.
- **Sigmoid**: Soft switch, turns on slowly (good for yes/no problems).
- **Tanh**: Like Sigmoid but centered around zero (better balance).
- **ReLU**: Simple switch, turns on only when positive (fast and effective).
- **Leaky ReLU**: Improved ReLU that never gets fully stuck.

We trained the same model with each switch and saw how well it worked. ReLU was the best, but Leaky ReLU also worked well.
