import random
from itertools import permutations

def boat_brute_force(x, y, z):
    result = ""
    perms = set(permutations([x, y, z]))
    ratings = [(abs(x[0] - x[2]), x) for x in perms]
    min_rating = min(ratings, key=lambda x: x[0])[0]
    best = [option[1] for option in ratings if option[0] == min_rating]
    for option in best:
        result += str(option) + "\n"
    return result

def boat_monte_carlo(x, y, z):
    best = []
    result = ""
    iterations = 10000
    for _ in range(iterations):
        perm = random.sample([x, y, z], k=3)
        rating = abs(perm[0] - perm[2])
        if not best or rating < best[0]:
            best = [rating, perm]
    result += "\n".join(str(option) for option in best[1])
    return result


def boat_heuristic(x, y, z):
    permutations = [(x, y, z), (x, z, y), (y, x, z)]
    best_solution = None
    min_imbalance = float('inf')
    for perm in permutations:
        imbalance = abs(sum(perm) - 240)
        if imbalance < min_imbalance:
            min_imbalance = imbalance
            best_solution = perm
    return [best_solution, best_solution[::-1]]


print("Brute Force:")
print(boat_brute_force(73, 85, 81))
print("\nMonte Carlo:")
print(boat_monte_carlo(73, 85, 81))
print("\nHeuristic:")
print(boat_heuristic(73, 85, 81))
