import program
import unittest

class TestSum(unittest.TestCase):
    def test_char(self):
        with self.assertRaises(TypeError):
            program.sum("a", "b")

if __name__ == '__main__':
    unittest.main()