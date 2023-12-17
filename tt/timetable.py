from itertools import permutations
import time
import multiprocessing


class Timetable:
    def __init__(self):
        self.table = {
            "Monday": ["WA", "WA", "C", "A", "M", None, "PV", "PV", None, None],
            "Tuesday": ["M", "TP", "DS", "DS", "A", "AM", None, "TV", None, None],
            "Wednesday": ["PIS", "C", "CIT", "CIT", "AM", "M", "DS", None, None, None],
            "Thursday": ["WA", "M", "PIS", "PV", "A", "C", "PSS", None, None, None],
            "Friday": [None, "PIS", "PIS", "A", "TV", "PSS", "PSS", None, None, None]
        }

    def generate_permutations(self):
        perm = permutations(["M", "DS", "DS", "PSS", "PSS", "A", None, "TV", None, None, "PIS", "M", "PIS", "PIS", "TP", "A", "CJ", None, None, None, "CIT", "CIT", "WA", "DS", "PV", None, "PSS", None, None, None, "AM", "M", "WA", "WA", None, "A", "C", "PIS", "TV", None, "C",   "A", "M", "PV", "PV", "AM", None, None, None, None])
        return perm

    def get_permutation_monday(self):
        tmp = list(permutations(self.table["Monday"]))
        return tmp

    def get_permutation_tuesday(self):
        tmp = list(permutations(self.table["Tuesday"]))
        return tmp

    def get_permutation_wednesday(self):
        tmp = list(permutations(self.table["Wednesday"]))
        return tmp

    def get_permutation_thursday(self):
        tmp = list(permutations(self.table["Thursday"]))
        return tmp

    def get_permutation_friday(self):
        tmp = list(permutations(self.table["Friday"]))
        return tmp

    def set_table(self):
        self.table["Monday"] = list(self.get_permutation_monday().pop(0))
        self.table["Tuesday"] = list(self.get_permutation_tuesday().pop(0))
        self.table["Wednesday"] = list(self.get_permutation_wednesday().pop(0))
        self.table["Thursday"] = list(self.get_permutation_thursday().pop(0))
        self.table["Friday"] = list(self.get_permutation_friday().pop(0))







t = Timetable()

index = 0
while True:
    print(list(t.get_permutation_monday().pop(0)))
    print(list(t.get_permutation_tuesday().pop(0)))
    print(list(t.get_permutation_wednesday().pop(0)))
    print(list(t.get_permutation_thursday().pop(0)))
    print(list(t.get_permutation_friday().pop(0)))
    print(index)
    index+= 1




if __name__ == "__main__":

    start = time.time()





"""
# Print original timetable
print("Puvodni rozvrh:")
for day in t.table:
    print(f"{t.table[day]}")
print("_______________________________________________________________")

index = 0
while True:
    t.set_table()
    for day in t.table:
        print(f"{t.table[day]}")
    print(index)
    index+=1
"""




