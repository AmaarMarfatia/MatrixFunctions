from subtract import subtract
import unittest

class TestSubtract(unittest.TestCase):

    def test_subtract(self):
        a = [[1, 2], [4, 5]]
        b = [[1, 2], [3, 4]]
        c = subtract(a, b)
        self.assertEqual(c, [[0, 0], [1, 1]])


if __name__ == '__main__':
    unittest.main()
