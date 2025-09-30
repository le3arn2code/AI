import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

# One-hot encode labels
encoder = OneHotEncoder()
y_encoded = encoder.fit_transform(y).toarray()

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Function to build MLP with given activation
def build_model(activation_function):
    model = Sequential()
    model.add(Dense(64, input_shape=(4,), activation=activation_function))
    model.add(Dense(64, activation=activation_function))
    model.add(Dense(3, activation='softmax'))  # 3 output classes
    model.compile(optimizer=Adam(),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Try different activations
activation_functions = ['sigmoid', 'tanh', 'relu']
results = {}

for func in activation_functions:
    print(f"\nTraining with {func} activation function")
    model = build_model(func)
    model.fit(X_train, y_train, epochs=50, batch_size=5,
              validation_split=0.1, verbose=0)
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    results[func] = accuracy
    print(f"Test Accuracy with {func}: {accuracy:.4f}")

print("\nResults Summary:", results)
