# Lab 32: Data Augmentation (Concept)
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras import models, layers

# Load a sample image (replace with your own if needed)
img_path = 'sample_image.jpg'
img = load_img(img_path)
x = img_to_array(img)
x = np.expand_dims(x, axis=0)

# Augmentation: rotation + flips
datagen = ImageDataGenerator(rotation_range=40, horizontal_flip=True, vertical_flip=True)

i = 0
for batch in datagen.flow(x, batch_size=1):
    plt.figure(i)
    plt.imshow(array_to_img(batch[0]))
    i += 1
    if i % 4 == 0:
        break
plt.show()

# Dummy dataset for demo model
X_train = np.random.rand(100, 64, 64, 3)
y_train = np.random.randint(0, 2, 100)
X_val = np.random.rand(20, 64, 64, 3)
y_val = np.random.randint(0, 2, 20)

# Simple CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("Training WITHOUT augmentation...")
history_no_aug = model.fit(X_train, y_train, epochs=5, validation_data=(X_val, y_val))

train_datagen = ImageDataGenerator(rotation_range=40, horizontal_flip=True, vertical_flip=True)
train_generator = train_datagen.flow(X_train, y_train, batch_size=16)

print("Training WITH augmentation...")
history_aug = model.fit(train_generator, epochs=5, validation_data=(X_val, y_val))

print("\nFinal Evaluation Without Augmentation:")
print("Accuracy:", history_no_aug.history['accuracy'][-1])
print("Validation Accuracy:", history_no_aug.history['val_accuracy'][-1])

print("\nFinal Evaluation With Augmentation:")
print("Accuracy:", history_aug.history['accuracy'][-1])
print("Validation Accuracy:", history_aug.history['val_accuracy'][-1])
