import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[-1, -1, -1], [-2, -2, -2], [-3, -3, -3]])

# Operace s maticemi x a y
result_addition = x + y  # sčítání
result_subtraction = x - y  # odčítání
result_elementwise_multiplication = x * y  # násobení prvků po prvcích
result_matrix_multiplication = x @ y  # maticové násobení

# Výpis výsledků
print("Addition result:")
print(result_addition)
print("\nSubtraction result:")
print(result_subtraction)
print("\nElementwise multiplication result:")
print(result_elementwise_multiplication)
print("\nMatrix multiplication result:")
print(result_matrix_multiplication)
