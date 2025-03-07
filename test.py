import unittest
import calculator

class TestMultiply(unittest.TestCase):

    def test_mult(self):
        self.assertEqual(calculator.calc(5,5), 25)
        
if __name__ == "__main__":
    unittest.main()
