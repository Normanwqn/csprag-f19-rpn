import unittest
import rpn


# Inherits the previously defined classes
class TestBasics(unittest.TestCase):
    # Declaring the name of this class
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)  # object. method
