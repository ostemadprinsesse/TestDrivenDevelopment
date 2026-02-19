import unittest

class TestIsUpperCase(unittest.TestCase):
    def test(self):
        self.assertEqual(makeUpperCase("apple"), "APPLE")


if __name__ == '__main__':    unittest.main()