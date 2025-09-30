from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Flatten, Dense

# Load the frozen base model
base_model = load_model("vgg16_base.h5")

# Build new model with custom layers
model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Save model
model.save("transfer_model.h5")
print("✅ Transfer learning model with custom layers saved as transfer_model.h5")
