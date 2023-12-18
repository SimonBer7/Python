import threading
from itertools import permutations
import time
import multiprocessing
from watchdog.dog import Watchdog


class Timetable:
    def __init__(self):
        self.table = {
            "Monday": ["WA", "WA", "C", "A", "M", None, "PV", "PV", None, None],
            "Tuesday": ["M", "TP", "DS", "DS", "A", "AM", None, "TV", None, None],
            "Wednesday": ["PIS", "C", "CIT", "CIT", "AM", "M", "DS", None, None, None],
            "Thursday": ["WA", "M", "PIS", "PV", "A", "C", "PSS", None, None, None],
            "Friday": [None, "PIS", "PIS", "A", "TV", "PSS", "PSS", None, None, None]
        }
        self.mon = set(self.get_permutation_monday())
        self.tue = set(self.get_permutation_tuesday())
        self.wed = set(self.get_permutation_wednesday())
        self.thu = set(self.get_permutation_thursday())
        self.fri = set(self.get_permutation_friday())

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

    def max(self):
        tmp = len(self.mon)+len(self.tue)+len(self.wed)+len(self.thu)+len(self.fri)
        return tmp



def main():
    t = Timetable()
    print("Pocet rozvrhu: "+str(t.max()**5))  # Return the result instead of printing



if __name__ == "__main__":
    watchdog = Watchdog(timeout_seconds=60)
    watchdog.start()

    p = multiprocessing.Process(target=main)
    p.start()
    p.join()

    if watchdog.check_timeout():
        print("Watchdog: Timeout occurred. Terminating the process.")
    else:
        print("Watchdog: Task completed within the timeout.")



"""
    while True:
        list(t.mon.pop())
        list(t.tue.pop())
        list(t.wed.pop())
        list(t.thu.pop())
        list(t.fri.pop())
        print(index)
        index+= 1
"""




