import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Reshape
reshaped_array = arr1.reshape(5, 1)
print("Reshaped Array:")
print(reshaped_array)

# Mean
mean_value = np.mean(arr1)
print("Mean:", mean_value)

# Sum
total_sum = np.sum(arr2)
print("Total Sum:", total_sum)
