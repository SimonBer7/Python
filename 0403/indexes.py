import numpy as np

# Matica x
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# a) Vypsání čísla na pozici [0, 0]
result_a = x[0, 0]
print("a) Number at position [0, 0]:", result_a)

# b) Vypsání celého druhého řádku
result_b = x[1, :]
print("b) Second row:", result_b)

# c) Vypsání prvního až druhého řádku
result_c = x[0:2, :]
print("c) First to second row:", result_c)

# d) Opět provedeme stejné úkoly, ale s použitím kratšího zápisu
result_d_a = x[0, 0]
result_d_b = x[1, :]
result_d_c = x[0:2, :]
print("\nd) Results using shorter notation:")
print("   a) Number at position [0, 0]:", result_d_a)
print("   b) Second row:", result_d_b)
print("   c) First to second row:", result_d_c)

# e) Vypsání prvků větších než 5
result_e = x[x > 5]
print("\ne) Elements greater than 5:", result_e)
