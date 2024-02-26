import time
import tracemalloc

from algoritmy import boat_brute_force, boat_monte_carlo, boat_heuristic

tracemalloc.start()
startTime = time.time()
result = boat_brute_force(73, 85, 81, 95)
timeConsupmtion = (time.time() - startTime) * 1000
memoryConsumption = tracemalloc.get_tracemalloc_memory()
tracemalloc.stop()

#print("Brute force: "+str(result))
print("Spotreba pameti: " + str(memoryConsumption) + " Bytes")
print("Spotreba casu: " + str(timeConsupmtion) + " milisec\n")

tracemalloc.start()
startTime = time.time()
result = boat_monte_carlo(73, 85, 81, 84, 86, 89)
timeConsupmtion = (time.time() - startTime) * 1000
memoryConsumption = tracemalloc.get_tracemalloc_memory()
tracemalloc.stop()

#print("Monte carlo: "+str(result))
print("Spotreba pameti: " + str(memoryConsumption) + " Bytes")
print("Spotreba casu: " + str(timeConsupmtion) + " milisec\n")

tracemalloc.start()
startTime = time.time()
result = boat_heuristic(73, 85, 81)
timeConsupmtion = (time.time() - startTime) * 1000
memoryConsumption = tracemalloc.get_tracemalloc_memory()
tracemalloc.stop()

print("Heuristic: "+str(result))
print("Spotreba pameti: " + str(memoryConsumption) + " Bytes")
print("Spotreba casu: " + str(timeConsupmtion) + " milisec\n")

