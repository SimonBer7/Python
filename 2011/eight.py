def vydej_obedu():
    napoj = ["vitamínový nápoj"]
    jidloA = ["polévka česneková s bramborem", "segedínský guláš, houskové knedlíky", "jablko"]
    jidloB = ["polévka česneková s bramborem", "kaše s bramborem", "hruška"]

    yield napoj

    volba = yield

    if(volba =="B"):
        yield jidloA
    else:
        yield jidloB


corutina1 = vydej_obedu()   #nastartuje corutinu
print(next(corutina1))      #spusti prvni cast
next(corutina1)             #spusti druhou cast, ktera ocekava data
print(corutina1.send("A"))  #posle data a nacte si vysledek
corutina1.close()           #ukonci corutinu
