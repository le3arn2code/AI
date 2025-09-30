# Interview Q&A - Activation Functions

1. **Why do we need activation functions in neural networks?**
   - They introduce non-linearity, allowing networks to learn complex patterns.

2. **When would you use Sigmoid activation?**
   - Useful for binary classification tasks.

3. **What is the main drawback of Sigmoid?**
   - Vanishing gradients and saturation.

4. **What is Tanh activation’s advantage over Sigmoid?**
   - Tanh outputs values between -1 and 1, making it zero-centered.

5. **Why is ReLU the most commonly used activation?**
   - Simple, efficient, and avoids vanishing gradients.

6. **What problem does ReLU face?**
   - The "dying ReLU" problem when neurons output zero constantly.

7. **How does Leaky ReLU solve the dying ReLU problem?**
   - It allows a small gradient for negative inputs.

8. **What is the impact of activation choice on model convergence?**
   - Some functions converge faster (ReLU), while others may slow learning (Sigmoid).

9. **Can we mix different activation functions in one network?**
   - Yes, sometimes different layers use different activations for performance tuning.

10. **What happens if we remove activation functions altogether?**
   - The network becomes a linear model, unable to capture complex relationships.
