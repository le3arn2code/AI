from keras.datasets import mnist
import matplotlib.pyplot as plt

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(f"Training data shape: {train_images.shape}")
print(f"Test data shape: {test_images.shape}")

# Show the first image
plt.imshow(train_images[0], cmap='gray')
plt.title(f"Label: {train_labels[0]}")
plt.savefig("mnist_sample.png")  # Save instead of showing (for VM use)
