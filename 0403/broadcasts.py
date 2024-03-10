import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

result_a = x * [0, 1, 0]
print(str(result_a)+"\n")

result_b = x * [[0], [1], [0]]
print(str(result_b)+"\n")

x[1] = 99
print(x[1])

x += 1  # přičtení 1 ke všem prvkům matice x
x -= 1  # odečtení 1 od všech prvků matice x
x *= 2  # vynásobení všech prvků matice x dvěma
x / 2  # vydělení všech prvků matice x dvěma

print(x)