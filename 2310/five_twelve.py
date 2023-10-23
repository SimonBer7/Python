import re

class PenezniHotovost:
    """
    Trida reprezentuje penezni hotovost v urcite mene
    """

    def __init__(self, castka: float, mena: str):
        """
        Pri vytvoreni tridy se musi specifikovat castka a mena, nebo se pouzije defaultnich 0 EUR

        :param castka: Jakekoli realne cislo, muze byt i zaporne
        :param mena: Mena vyjadrena jako tripismeny kod
        :return: Objekt penezni hotovosti
        """
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._mena = mena
        self._castka = castka

    def __str__(self):
        """
        Vrati castku a menu jako string
        :return: <castka> <mena>
        """
        return str(self._castka)+" "+self._mena

    def __add__(self, other):
        """
        Pretizeni operatoru + ktere vytvori novy objekt jako vysledek operace scitnai
        :param other: Lze scitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")


    def __sub__(self, other):
        if (isinstance(other, float) or isinstance(other, int)) and self._mena == 'CZK':
            vysledek = PenezniHotovost(self._castka - other, self._mena)
            return vysledek

        elif isinstance(other, PenezniHotovost) and other._mena == self._mena:
            vysledek = PenezniHotovost(self._castka - other._castka, self._mena)
            return vysledek

        raise Exception("Error, lze odecist pouze int nebo float.")


    def __mul__(self, other):
        if (isinstance(other, float)) or (isinstance(other, int)):
            vysledek = PenezniHotovost(self._castka * other, self._mena)
            return vysledek
        else:
            raise Exception("Error, lze nasobit jen int nebo float")

    def __pow__(self, power, modulo=None):
        if (isinstance(power, int)):
            vysledek = PenezniHotovost(self._castka ** power, self._mena)
            return vysledek
        else:
            raise Exception("Error, mocnitel musi byt int")


sto_korun = PenezniHotovost(100, "CZK")
dve_sta_korun = sto_korun + 100

print(sto_korun)
print(dve_sta_korun)



