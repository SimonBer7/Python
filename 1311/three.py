class ZvysitelnaUrovenInterface:
    def zvysitUroven(self):
        raise NotImplementedError()

class Bojovnik(ZvysitelnaUrovenInterface):
    MAX_SILA = 3

    def __init__(self, sila):
        if type(sila) is not int or sila < 0 or sila > self.MAX_SILA:
            raise Exception("Sila bojovnika není v povoleném rozmezí")

        self.sila = sila

    def zvysitUroven(self):
        if self.sila < self.MAX_SILA:
            self.sila += 1

class Mag(ZvysitelnaUrovenInterface):
    def __init__(self, bilaMagie, cernaMagie):
        if type(bilaMagie) is not bool:
            raise Exception("Bila magie musí být True/False")
        if type(cernaMagie) is not bool:
            raise Exception("Cerna magie musí být True/False")

        self.cernaMagie = cernaMagie
        self.bilaMagie = bilaMagie

    def zvysitUroven(self):
        if not self.bilaMagie:
            self.bilaMagie = True
        elif not self.cernaMagie:
            self.cernaMagie = True

# Testování
bobik = Bojovnik(1)
bobik.zvysitUroven()
print(bobik.sila)  # Výstup by měl být 2

martina = Mag(True, False)
martina.zvysitUroven()
print(martina.cernaMagie)  # Výstup by měl být True
