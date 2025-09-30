import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load data
(X_train, y_train), (X_val, y_val) = mnist.load_data()

# Preprocess data
X_train = X_train.reshape(X_train.shape[0], -1).astype('float32') / 255
X_val = X_val.reshape(X_val.shape[0], -1).astype('float32') / 255

y_train = to_categorical(y_train)
y_val = to_categorical(y_val)

# Define model
model = Sequential()
model.add(Dense(512, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=3)

# Train
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50,
                    batch_size=200, callbacks=[early_stopping], verbose=2)
