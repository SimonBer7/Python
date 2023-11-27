
vysledky = [
    ("Karel", 31),
    ("Petr", 10),
    ("Honza", 52),
    ("Eva", 61),
    ("Katka", 0),
]

results = sorted(vysledky, key=lambda x: x[1])

for jmeno, body in results:
    print(f"{jmeno}: {body} body")


