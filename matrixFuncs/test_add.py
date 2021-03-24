from add import add
import unittest

class TestAdd(unittest.TestCase):

    def test_2by2(self):
        a = [[1, 2], [4, 5]]
        b = [[1, 2], [3, 4]]
        c = add(a, b)
        self.assertEqual(c, [[2, 4], [7, 9]])

    def test_3by3(self):
        d = [[1,2,3],[4,5,6],[7,8,9]]
        e = [[4,5,6],[7,8,9],[1,2,3]]
        f = add(d,e)
        self.assertEqual(f, [[5,7,9],[11,13,15],[8,10,12]])

    def test_rectange(self):
        g = [[1, 2, 3], [4, 5, 6]]
        h = [[1, 2, 3], [4, 5, 6]]
        i = add(g,h)
        self.assertEqual(i, [[2,4,6],[8,10,12]])


if __name__ == '__main__':
    unittest.main()
