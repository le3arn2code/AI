from tensorflow.keras.applications import VGG16

# Load the VGG16 model without the top classification layer
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze layers to prevent retraining them
for layer in base_model.layers:
    layer.trainable = False

# Save the base model for later use
base_model.save("vgg16_base.h5")
print("✅ VGG16 base model saved as vgg16_base.h5")
