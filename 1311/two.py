import re

class Zbozi:
    def __init__(self, nazev, cena):
        if type(nazev) is not str or not re.match(r"[a-zA-Z]{2,50}", nazev):
            raise Exception('Nazev musi byt 2-50 znaku')
        if (type(cena) is not float and type(cena) is not int) or cena < 0:
            raise Exception('Cena musi byt kladne cislo')
        self._nazev = nazev
        self._cena = cena

    def get_cena(self):
        return self._cena

class ZlevneneZbozi(Zbozi):
    def __init__(self, nazev, cena, sleva):
        super().__init__(nazev, cena)
        if type(sleva) is not float or sleva < 0 or sleva > 0.5:
            raise Exception('Sleva musi byt cislo od 0.0 do 0.5')
        self._sleva = sleva

    def get_cena(self):
        cena_po_sleve = self._cena * (1 - self._sleva)
        return cena_po_sleve

# Příklad použití
zlevnene_zbozi = ZlevneneZbozi("Kniha", 100, 0.2)
print("Původní cena:", zlevnene_zbozi.get_cena())  # Výstup by měl být 80.0 (80% ceny původního zboží)
