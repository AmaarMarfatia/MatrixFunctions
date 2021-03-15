from add import add
import unittest

class TestAdd(unittest.TestCase):

    def test_multi(self):
        a = [[1, 2], [4, 5]]
        b = [[1, 2], [3, 4]]
        c = add(a, b)
        self.assertEqual(c, [[2, 4], [7, 9]])

        d = [[1,2],[3,4]]
        e = [[5,6],[7,8]]

        f = [[1,2,3],[4,5,6],[7,8,9]]
        g = [[4,5,6],[7,8,9],[1,2,3]]

        h = [[1, 2, 3], [4, 5, 6]]
        i = [[1, 2, 3], [4, 5, 6]]


if __name__ == '__main__':
    unittest.main()
