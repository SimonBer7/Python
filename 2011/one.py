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
    raise StopIteration()


""""
print("Krasjova jezera v CR")
for jezero in generatorKrasovychJezerCR():
    print(jezero)
"""

print("Raselinna jezera v CR: \n")
for jezero in generatorRaselinovychJezer():
    print(jezero)
