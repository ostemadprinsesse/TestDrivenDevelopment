import unittest
import math
from app import multiplication


class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(2), 4)
        
    def test_multiplication_negativ(self):
        self.assertEqual(multiplication(-3), 9)
        
    def test_multiplication_zero(self):    
        self.assertEqual(multiplication(0), 0)

if __name__ == '__main__':    unittest.main()