
zbozi = [
    {
        "name" : "IPHONE 14",
        "price" : 22169.0,
        "cathegory" : (12, "Mobilní telefony")
    },
    {
        "name" : "Fujifilm XT30",
        "price" : 22269.0,
        "cathegory" : (2, "Fotoaparáty")
    },
    {
        "name" : "Niceboy HIVE Pins Black",
        "price" : 999.0,
        "cathegory" : (4, "Sluchátka")
    }
]

results_by_price = sorted(zbozi, key=lambda x: x["price"])
results_by_name = sorted(zbozi, key=lambda x: x["name"])
results_by_cathegory = sorted(zbozi, key=lambda x: x["cathegory"], reverse=True)

for item in results_by_price:
    print(item)

print()
for item in results_by_name:
    print(item)

print()
for item in results_by_cathegory:
    print(item)


