import unittest
import rpn


# Inherits the previously defined classes
class TestBasics(unittest.TestCase):
    # Declaring the name of this class
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)  # object. method
    def test_sub(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)  # object. method
    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')
    def test_mul(self):
        result = rpn.calculate('12 8 *')
        self.assertEqual(96, result)
    def test_div(self):
        result = rpn.calculate('12 8 /')
        self.assertEqual(1, result)
    def test_div2(self):
        result = rpn.calculate('24 8 /')
        self.assertEqual(3, result)

