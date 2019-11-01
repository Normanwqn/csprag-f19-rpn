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