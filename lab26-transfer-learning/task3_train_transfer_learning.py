import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# ✅ Enable eager execution for numpy() support
tf.config.run_functions_eagerly(True)

# Load the model without optimizer state
model = load_model("transfer_model.h5", compile=False)

# Recompile with fresh optimizer
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255)
train_data_path = '/home/toor/datasets/cats_and_dogs_filtered/train'

train_generator = train_datagen.flow_from_directory(
    train_data_path,
    target_size=(224, 224),
    batch_size=20,
    class_mode='binary'
)

# Train
history = model.fit(
    train_generator,
    steps_per_epoch=50,
    epochs=3,
    verbose=1
)

# Plot results
acc = history.history['accuracy']
loss = history.history['loss']
plt.plot(acc, label="Accuracy")
plt.plot(loss, label="Loss")
plt.legend()
plt.title("Transfer Learning Training")
plt.savefig("transfer_learning_training.png")  # ✅ Save instead of show
print("✅ Training plot saved as transfer_learning_training.png")
