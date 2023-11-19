class A:
    def test(self):
        print("Metoda test třídy A")

class B:
    def test(self):
        print("Metoda test třídy B")

class C(A, B):
    pass

# 1
instance_c = C()
instance_c.test()
