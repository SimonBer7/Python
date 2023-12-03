import unittest
import random
import time


class Prvek:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.dalsi = None

class Zasobnik:
    def __init__(self):
        self.vrchol = None
        self.pocet_prvku = 0

    def add(self, hodnota):
        novy_prvek = Prvek(hodnota)
        novy_prvek.dalsi = self.vrchol
        self.vrchol = novy_prvek
        self.pocet_prvku += 1

    def pop(self):
        if self.pocet_prvku == 0:
            raise Exception("Zásobník je prázdný")
        vrcholni_prvek = self.vrchol
        self.vrchol = vrcholni_prvek.dalsi
        self.pocet_prvku -= 1
        return vrcholni_prvek.hodnota

    def count(self):
        return self.pocet_prvku

    def clear(self):
        self.vrchol = None
        self.pocet_prvku = 0

    def popAll(self, as_tuple=False):
        prvky = []
        while self.pocet_prvku > 0:
            hodnota = self.pop()
            prvky.append(hodnota)
        if as_tuple:
            return tuple(prvky)
        return prvky


class TestZasobnik(unittest.TestCase):

    def setUp(self):
        self.zasobnik = Zasobnik()

    def test_add_and_pop(self):
        self.zasobnik.add(42)
        self.assertIn(42, self.zasobnik.popAll())

    def test_pop_empty_stack(self):
        with self.assertRaises(Exception):
            self.zasobnik.pop()

    def test_count(self):
        self.assertEqual(self.zasobnik.count(), 0)
        self.zasobnik.add(10)
        self.zasobnik.add(20)
        self.assertEqual(self.zasobnik.count(), 2)

    def test_clear(self):
        self.zasobnik.add(1)
        self.zasobnik.add(2)
        self.zasobnik.clear()
        self.assertEqual(self.zasobnik.count(), 0)

    def test_pop_all_as_tuple(self):
        self.zasobnik.add(1)
        self.zasobnik.add(2)
        result = self.zasobnik.popAll(as_tuple=True)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (2, 1))

    def test_not_in_empty_stack(self):
        self.assertNotIn(42, self.zasobnik.popAll())

    """"
    def test_performance(self):
        start_time = time.time()
        for _ in range(1000000):
            self.zasobnik.add(random.randint(1, 999))
        elapsed_time = time.time() - start_time
        self.assertLess(elapsed_time, 0.5)
    """

if __name__ == '__main__':
    unittest.main()