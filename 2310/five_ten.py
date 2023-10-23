class Zbozi:
    def __new__(cls, nazev, cena):
        if not isinstance(nazev, str) or not isinstance(cena, (int, float)) or cena < 0:
            raise ValueError("Error, neplatné hodnoty")
        else:
            instance = super().__new__(cls)
        return instance

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

a = Zbozi("Rohlik", 5)
b = Zbozi("Hackers item", 10)

print(a)
print(b)
