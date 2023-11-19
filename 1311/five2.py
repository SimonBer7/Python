class A:
    def __init__(self):
        self.a_variable = True

    def test(self):
        print("Metoda test třídy A")

class B:
    def __init__(self):
        self.b_variable = True

    def test(self):
        print("Metoda test třídy B")

class C(A, B):
    def __init__(self):
        super().__init__()

# 2
instance_c = C()
print(instance_c.a_variable)  # Výstup by měl být True
print(hasattr(instance_c, 'b_variable'))  # Výstup by měl být False, protože konstruktor třídy B nebyl volán
