
from itertools import permutations

def boat_brute_force(x, y, z):
    best = []
    i = 0
    result = ""
    list = set(permutations([x, y, z]))
    ratings = [(abs(x[0] - x[2]), x) for x in list]
    for option in ratings:
        if option[0] == min(ratings)[0]:
            best.append(option)
        i += 1
    for option in best:
        result += str(option[1])+"\n"
    return result


def boat_monte_carlo(x, y, z):
    list = [x, y, z]
    for i in len(list):

        list.shuffle()



def boat_heuristic(x, y, z):
    pass



print(boat_brute_force(73, 85, 81))




