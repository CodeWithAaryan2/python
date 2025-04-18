import numpy as np

# Creating two arrays of the same shape
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[6, 5, 4], [3, 2, 1]])

# Element-wise operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

# Printing results
print("Element-wise Addition:\n", addition)

print("Element-wise Subtraction:\n", subtraction)
print("Element-wise Multiplication:\n", multiplication)
print("Element-wise Division:\n", division)

# Define two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Dot product
dot_product = np.dot(vector1, vector2)
print("Dot Product:", dot_product)

# Cross product
cross_product = np.cross(vector1, vector2)
print("Cross Product:\n", cross_product)