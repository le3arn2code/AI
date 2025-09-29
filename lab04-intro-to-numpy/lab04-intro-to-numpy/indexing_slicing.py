import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Access element
element = arr1[2]
print("Accessed Element:", element)

# Slice subset
subarray = arr2[0:2, 1:3]
print("Sliced Array:")
print(subarray)
