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

# Build model with LeakyReLU
def build_model_leakyrelu():
    model = Sequential()
    model.add(Dense(64, input_shape=(4,)))
    model.add(tf.keras.layers.LeakyReLU(alpha=0.01))
    model.add(Dense(64))
    model.add(tf.keras.layers.LeakyReLU(alpha=0.01))
    model.add(Dense(3, activation='softmax'))
    model.compile(optimizer=Adam(),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

print("\nTraining with LeakyReLU activation function")
model = build_model_leakyrelu()
model.fit(X_train, y_train, epochs=50, batch_size=5,
          validation_split=0.1, verbose=0)
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy with Leaky ReLU: {accuracy:.4f}")
