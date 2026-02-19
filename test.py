import unittest
import math

class TestKvadrot(unittest.TestCase):
    def test_kvadrot(self):
        self.assertEqual(kvadrot(2), 4)
        
    def test_kvadrot_negativ(self):
        self.assertEqual(kvadrot(-3), 9)
        
    def test_kvadrot_zero(self):    
        self.assertEqual(kvadrot(0), 0)

if __name__ == '__main__':    unittest.main()