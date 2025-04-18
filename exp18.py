import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Reshaping 1D to 2D
reshaped_array = array_1d.reshape(5, 1)

# Slicing 2D array
sliced_array = array_2d[:2, :2]

# Indexing an element
indexed_element = array_2d[1, 2]

print("1D Array:", array_1d)
print("2D Array:", array_2d)
print("3D Array:", array_3d)
print("Reshaped 1D to 2D:", reshaped_array)
print("Sliced 2D Array:", sliced_array)
print("Indexed Element:", indexed_element)