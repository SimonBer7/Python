import numpy as np

# Vytvoření matice s nulovými hodnotami o rozměru 3x3
zeros_matrix = np.zeros((3, 3))
print("Matrix of zeros:")
print(zeros_matrix)

# Vytvoření matice s jedničkovými hodnotami o rozměru 3x3
ones_matrix = np.ones((3, 3))
print("\nMatrix of ones:")
print(ones_matrix)

# Vytvoření matice s hodnotou 3148 o rozměru 3x3
custom_value_matrix = np.full((3, 3), 3148)
print("\nMatrix filled with custom value:")
print(custom_value_matrix)

# Vytvoření jednotkové čtvercové matice o rozměru 3x3
identity_matrix = np.eye(3)
print("\nIdentity matrix:")
print(identity_matrix)

# Vytvoření diagonální matice s danými prvky na diagonále
diagonal_matrix = np.diag([1, 2, 3, 4])
print("\nDiagonal matrix:")
print(diagonal_matrix)

# Vytvoření číselné řady od 0 do 49
number_series = np.arange(50)
print("\nNumber series:")
print(number_series)
