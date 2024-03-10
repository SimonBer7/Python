import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the shape of the array
shape_of_x = x.shape

# Get the data type of the array
data_type_of_x = x.dtype

# Print the shape and data type of the array
print("Shape of x:", shape_of_x)
print("Data type of x:", data_type_of_x)

result_a = x - 1
print(result_a.dtype)
result_b = x + 1
print(result_b.dtype)
result_c = x * 2
print(result_c.dtype)
result_d = x / 2
print(result_d.dtype)
result_e = x > 5
print(result_e.dtype)
result_f = (x > 5) & (x < 8)
print(result_f.dtype)
result_g = (x < 2) | (x > 7)
print(result_g.dtype)