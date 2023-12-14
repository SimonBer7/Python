from itertools import permutations

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

t = Timetable()

# Print original timetable
#for day in t.table:
#    print(f"{day}: {t.table[day]}")

index = 0
for i in t.generate_permutations():
    print(i)
    index+=1
    print(index)