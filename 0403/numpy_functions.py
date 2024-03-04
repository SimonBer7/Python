import numpy as np

brute_force = np.array([1, 2, 3, 0.1932, 1.1247, 2.2435, 2243, 2124, 2143])

'''
RESHAPE
'''
new_array = brute_force.reshape(3, 3, 1)
#print("Reshaped numpy array: \n", new_array)

'''
SPLIT
'''

size, time, memory = np.array_split(brute_force, 3)
connected_array = np.concatenate((size, time, memory))

print("Puvodni pole:", brute_force)
print("Oddelene pole 'velikost':", size)
print("Oddelene pole 'spotreba casu':", time)
print("Oddelene pole 'spotreba pameti':", memory)
print("Spojene pole:", connected_array)

'''
Př. se zasobnikem
'''
vysledek = np.stack((size, time, memory), axis=1)
vysledek = np.vstack((size, time, memory))
vysledek = np.hstack((size, time, memory))
vysledek = np.dstack((size, time, memory))

print("\n", vysledek)


