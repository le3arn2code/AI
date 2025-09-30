from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# Reshape
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Build CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(train_images, train_labels, epochs=5, batch_size=64, verbose=2)

# Evaluate
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"✅ Test accuracy: {test_acc:.4f}")
