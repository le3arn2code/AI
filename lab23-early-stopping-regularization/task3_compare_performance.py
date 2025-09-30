import matplotlib.pyplot as plt

# Assumes histories 'history' and 'history_reg' are available after running tasks 1 and 2
plt.plot(history.history['val_loss'])
plt.plot(history_reg.history['val_loss'])
plt.title('Model validation loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Model without L2', 'Model with L2'], loc='upper left')
plt.savefig('compare_validation_loss.png')
