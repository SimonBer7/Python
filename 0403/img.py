from PIL import Image
import numpy as np

# Načtení obrázku
img = Image.open("8a68f104fc2394e6cca08922bbecf6d2.jpg")

# Převod obrázku na matici
matrix = np.asarray(img)

# Zjištění vlastností matice
print("Shape (tvar) of the matrix:", matrix.shape)
print("Data type of the matrix:", matrix.dtype)

# Zobrazení matice (prvních 5 řádků a sloupců)
print("Matrix:")
print(matrix[:5, :5])
