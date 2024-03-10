import numpy as np

# a) Vygenerujte jedno náhodné celé číslo
random_integer = np.random.randint(100)  # Generuje náhodné celé číslo od 0 do 99
print("Random integer:", random_integer)

# b) Vygenerujte jedno náhodné desetinné číslo
random_float = np.random.random()  # Generuje náhodné desetinné číslo mezi 0 a 1
print("Random float:", random_float)

# c) Vygenerujte jednorozměrné pole náhodných čísel o velikosti 100 prvků
random_array = np.random.rand(100)  # Generuje pole náhodných čísel o velikosti 100
print("Random array:", random_array)

# d) Vygenerujte matici náhodných čísel o velikosti 10x10 prvků
random_matrix = np.random.rand(10, 10)  # Generuje matici náhodných čísel o rozměrech 10x10
print("Random matrix:")
print(random_matrix)

# e) Vygenerujte náhodnou hodnotu z pole [21,22,34,56]
choices = [21, 22, 34, 56]
random_choice = np.random.choice(choices)  # Náhodně vybírá hodnotu z daného pole
print("Random choice:", random_choice)

# f) Vygenerujte 15 známek z předmetu Matematika na naší škole s danými pravděpodobnostmi
grades = [1, 2, 3, 4, 5]
probabilities = [0.10, 0.25, 0.25, 0.28, 0.12]
random_grades = np.random.choice(grades, 15, p=probabilities)  # Generuje 15 známek s danými pravděpodobnostmi
print("Random grades:", random_grades)
