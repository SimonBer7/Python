
def generatorKrasovychJezerCR():
    yield "Horní macošské jezírko"
    yield "Dolní macošské jezírko"
    yield "jezírko v Hranické propasti"
    yield "Bozkovské podzemní jezero"
    yield "Točnické jezírko"
    raise StopIteration()


def generatorRaselinovychJezer():
    yield "Chalupské jezírko"
    yield "Velké mechové jezírko"
    yield "Jezírko pod Táborem"
    yield "Malé mechové jezírko"


print("Raselinna jezera v CR: \n")
raselinna_jezera = generatorRaselinovychJezer()

while True:
    try:
        jezero = next(raselinna_jezera)
        print(jezero)
    except StopIteration:
        break



