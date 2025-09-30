from keras.models import load_model
from keras.datasets import mnist
from keras.utils import to_categorical

# Load dataset
(_, _), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1) / 255.0
y_test = to_categorical(y_test)

# Load model
model = load_model("cnn_mnist.h5")

# Evaluate
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")
