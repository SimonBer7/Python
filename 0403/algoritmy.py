import numpy as np


brute_force = np.array([[0, 12, 50], [0.2, 1.4412, 1.94724], [0, 2, 6]])
monte_carlo = np.array([[0, 8, 40], [0.22, 0.21, 0.22], [0, 1, 5]])
heuristic = np.array([[0, 7, 35], [0.2, 0.342, 0.44], [0, 1, 4]])

print("Brute force, časová složitost [sec]: "+str(brute_force[1]))
print("Monte carlo, časová složitost [sec]: "+str(monte_carlo[1]))
print("Heuristika, časová složitost [sec]: "+str(heuristic[1]))

print("Všechny prvky paměťové složitost brute force vyjma prvního a posledního:")
print(brute_force[1, 1:-1])

print("\nPosledních 5 prvků časové složitost monte carlo:")
print(monte_carlo[0, -5:])


print("\nPrvní prvek počtu sedadel, který jste měřili heuristice:")
print(heuristic[2, 0])

selected_array = brute_force

print("\nVlastnosti vybraného pole:")
print("Počet dimenzí:", selected_array.ndim)
print("Tvar pole (shape):", selected_array.shape)
print("Datový typ prvků:", selected_array.dtype)
print("Velikost prvků v bytech:", selected_array.itemsize)
print("Data pole:", selected_array.data)
