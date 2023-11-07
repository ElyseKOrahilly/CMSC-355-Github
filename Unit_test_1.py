import program
import unittest

class TestSum(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(program.sum(1, 1), 2)

if __name__ == '__main__':
    unittest.main()