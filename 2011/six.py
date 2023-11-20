
class GeneratorKrasovychJezer():

    def __init__(self):
        self.dyje = []
        self.labe = []
        self.bilina = []
        self.bez = []
        self.setValues()

    """
    jezera = [
        "Křivé jezero (Dyje)",
        "Květné jezero (Dyje)",
        "Kutnar (Dyje)",
        "Mahenovo jezero (Dyje)",
        "Babinecká tůň (Labe)",
        "Hrbáčkovy tůně (Labe)",
        "Komořanské jezero (Bílina - zaniklo 1831)",
        "Antošovické jezero",
        "Holásecká jezera",
        "Krňák",
        "Kurfürstovo rameno",
        "Malá říčka",
        "Podhradská tůň"
    ]
    """
    
    jezera = [
        ["Dyje", ["Křivé jezero","Květné jezero","Kutnar","Mahenovo jezero"]],
        ["Labe", ["Babinecká tůň","Hrbáčkovy tůně"]],
        ["Bílina", ["Komořanské jezero"]],
        ["(bez řeky)", ["Antošovické jezero", "Holásecká jezera","Krňák","Kurfürstovo rameno","Malá říčka","Podhradská tůň"]]
    ]

    def setValues(self):
        for list in GeneratorKrasovychJezer.jezera:
            if list[0] == "Dyje":
                self.dyje = list[1]
            if list[0] == "Labe":
                self.labe = list[1]
            if list[0] == "Bílina":
                self.bilina = list[1]
            if list[0] == "(bez řeky)":
                self.bez = list[1]


    def __str__(self):
        print = ""
        for jezero in self.dyje:
            print += str(jezero)+" (Dyje)\n"

        for jezero in self.labe:
            print += str(jezero)+" (Labe)\n"

        for jezero in self.bilina:
            print += str(jezero)+" (Bilina)\n"

        for jezero in self.bez:
            print += str(jezero)+"\n"
        return print

    def __iter__(self):
        self.i = 0;
        return self

    def __next__(self):
        if self.i > (len(GeneratorKrasovychJezer.jezera)-1):
            raise StopIteration()

        pomocnaPromenna = GeneratorKrasovychJezer.jezera[self.i]
        self.i = self.i + 1
        return pomocnaPromenna

gen = GeneratorKrasovychJezer()

print(gen)


