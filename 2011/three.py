
def generatorITVelikanu():
    yield "Steve Jobs"
    yield "Richard Stallman"
    yield "Bill Gates"
    yield "Steve Wozniak"


print("Velikani v IT: \n")
for osoba in generatorITVelikanu():
    print(osoba)
