import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.regularizers import l2
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load data
(X_train, y_train), (X_val, y_val) = mnist.load_data()

# Preprocess
X_train = X_train.reshape(X_train.shape[0], -1).astype('float32') / 255
X_val = X_val.reshape(X_val.shape[0], -1).astype('float32') / 255

y_train = to_categorical(y_train)
y_val = to_categorical(y_val)

# Model with L2
model_reg = Sequential()
model_reg.add(Dense(512, input_dim=784, activation='relu', kernel_regularizer=l2(0.01)))
model_reg.add(Dense(10, activation='softmax'))

model_reg.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history_reg = model_reg.fit(X_train, y_train, validation_data=(X_val, y_val),
                            epochs=50, batch_size=200, verbose=2)
