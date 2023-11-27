
import unittest

class Lahev:
    def __init__(self, kapacita):
        self.kapacita = kapacita
        self.objem_litry = 0
        self.zavrena = True

    def set_objem_litry(self, novy_objem):
        if self.zavrena:
            print("Láhev je zavřená, nelze měnit objem kapaliny.")
        else:
            self.objem_litry = min(novy_objem, self.kapacita)

    def get_objem_litry(self):
        return self.objem_litry

    def set_objem_mililitry(self, novy_objem):
        self.set_objem_litry(novy_objem / 1000)

    def get_objem_mililitry(self):
        return self.objem_litry * 1000

    def clear_bottle(self):
        if self.zavrena:
            print("Láhev je zavřená, nelze vyprázdnit obsah.")
        else:
            self.objem_litry = 0

    def close_bottle(self):
        self.zavrena = True
        print("Láhev je nyní zavřená.")

    def open_bottle(self):
        self.zavrena = False
        print("Láhev je nyní otevřená.")


class TestBottleMethods(unittest.TestCase):

    def test_init(self):
        lahev = Lahev(5)
        self.assertEqual(lahev.kapacita, 5)
        self.assertEqual(lahev.objem_litry, 0)
        self.assertTrue(lahev.zavrena)

    def test_set_objem_litry(self):
        lahev = Lahev(5)
        lahev.open_bottle()
        lahev.set_objem_litry(2)
        self.assertEqual(lahev.get_objem_litry(), 2)

    def test_set_objem_ml(self):
        lahev = Lahev(5)
        lahev.open_bottle()
        lahev.set_objem_mililitry(2)
        self.assertEqual(lahev.get_objem_mililitry(), 2)

    def test_clear_bottle(self):
        lahev = Lahev(5)
        lahev.open_bottle()
        lahev.set_objem_litry(2)
        lahev.clear_bottle()
        self.assertEqual(lahev.get_objem_litry(), 0)

    def test_close_bottle(self):
        lahev = Lahev(5)
        lahev.close_bottle()
        self.assertTrue(lahev.zavrena)

    def test_open_bottle(self):
        lahev = Lahev(5)
        lahev.open_bottle()
        self.assertFalse(lahev.zavrena)


if __name__ == '__main__':
    unittest.main()
