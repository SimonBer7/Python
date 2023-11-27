
pole = [100.10, 323.2, 355.9, 214.19, 87.0]

pole2 = list(map(lambda x: x *1.3, pole))
pole3 = list(filter(lambda x: x > 120, pole))
pole4 = list(map(lambda x: x *1.3 -5 if x* 1.3 > 110 else None, pole))
pole4 = list(filter(lambda x: x is not None, pole4))


print("Pole 2: ", pole2)
print("Pole 3: ", pole3)
print("Pole 4: ", pole4)
