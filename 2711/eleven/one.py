
import unittest

def add(a, b):
    return a+b

class TestMethods(unittest.TestCase):

    def testing_add_int(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def testing_add_float(self):
        result = add(5.5, 4.5)
        self.assertEqual(result, 10)

    def testing_add_complex(self):
        result = add(2 + 3j, 4 + 5j)
        self.assertEqual(result, 6 + 8j)

    def testing_error(self):
        result = add("ahoj", 4)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()



