import numpy as np

# Creating an array
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculating statistical measures
mean_value = np.mean(data) # Mean
median_value = np.median(data) # Median
std_dev = np.std(data) # Standard Deviation
variance = np.var(data) # Variance

# Creating two related datasets for correlation
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
correlation_matrix = np.corrcoef(x, y) # Correlation Coefficient

# Printing results
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Correlation Coefficients:")
print(correlation_matrix)