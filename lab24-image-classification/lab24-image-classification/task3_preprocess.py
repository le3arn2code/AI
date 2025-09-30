from keras.datasets import mnist

# Load dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# Reshape to add channel dimension
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

print("✅ Preprocessing done.")
print(f"Train shape: {train_images.shape}, Test shape: {test_images.shape}")
