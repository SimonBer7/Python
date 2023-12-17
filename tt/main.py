# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


from itertools import permutations


class Rozvrh:
    def __init__(self, rozvrh_data):
        self.rozvrh_data = rozvrh_data



def generuj_varianty( rozvrh):

    predmety_na_dny = [rozvrh.rozvrh_data[i:i + 10] for i in range(0, len(rozvrh.rozvrh_data), 10)]

    for den in predmety_na_dny:
        for permutace in permutations(den):
            index+=1
            yield list(permutace)


def main():
    # Předpokládáme, že máme již vytvořený rozvrh_data
    rozvrh_data = ["M", "DS", "DS", "PSS", "PSS", "A", None, "TV", None, None,
                   "PIS", "M", "PIS", "PIS", "TP", "A", "CJ", None, None, None,
                   "CIT", "CIT", "WA", "DS", "PV", None, "PSS", None, None, None,
                   "AM", "M", "WA", "WA", None, "A", "C", "PIS", "TV", None,
                   "C", "A", "M", "PV", "PV", "AM", None, None, None, None]

    rozvrh = Rozvrh(rozvrh_data)

    # Spustíme generátor variant rozvrhu
    for variant in generuj_varianty(rozvrh):
        print(variant)


if __name__ == "__main__":
    main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
