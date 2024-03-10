import numpy as np

# Pole obsahující jména kamarádů
kamaradi = np.array(["Alice", "Bob", "Charlie"])

# a) Náhodné seřazení pole kamarádů (změna v původním poli)
np.random.shuffle(kamaradi)
print("Random order of friends (in-place):", kamaradi)

# b) Náhodné seřazení pole kamarádů (bez změny v původním poli, vytvoření nového pole)
random_order = np.random.permutation(kamaradi)
print("Random order of friends (new array):", random_order)
