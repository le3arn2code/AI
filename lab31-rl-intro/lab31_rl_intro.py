#!/usr/bin/env python3
# Lab 31 — Introduction to Reinforcement Learning (FrozenLake) using Gymnasium

# Task 2.2: Initialize the Environment
import gymnasium as gym  # Maintained drop-in replacement for OpenAI Gym

# Initialize the FrozenLake environment (simplified: no stochastic slips)
env = gym.make('FrozenLake-v1', is_slippery=False)

# Task 2.3: Observe the Environment (initial state)
obs, info = env.reset()
print("Initial State:", obs)

# Task 3.1: Simulate a single action and observe results
# Sample a random action
action = env.action_space.sample()

# Apply the action in the environment (Gymnasium returns 5 values)
new_obs, reward, terminated, truncated, info = env.step(action)
done = terminated or truncated

# Display results
print("Action taken:", action)
print("New State:", new_obs)
print("Reward:", reward)
print("Episode Done:", done)

# Task 3.2: Loop to log actions and rewards (5 steps max)
for step in range(5):  # Run for 5 steps
    action = env.action_space.sample()
    new_obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
    print(f"Step {step}: Action: {action}, New State: {new_obs}, Reward: {reward}, Done: {done}")
    if done:
        print("Episode finished after {} steps".format(step + 1))
        break
