import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 6), 11)
        self.assertEqual(self.calc.add(3, 1),4)
    
    def test_add1(self):
        self.assertEqual(self.calc.add(5, 6), 11)

    def test_add2(self):
        self.assertEqual(self.calc.add(3, 1),4)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(13, 3), 1)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(33, 2), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()