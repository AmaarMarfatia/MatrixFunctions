from multiply import multiply
import unittest

class TestMultiply(unittest.TestCase):

    def test_rectangle(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[1, 2], [3, 4], [5, 6]]
        c = multiply(a, b)
        self.assertEqual(c, [[22, 28], [49, 64]])

    def test_square(self):
        d = [[1,2],[3,4]]
        e = [[5,6],[7,8]]
        f = multiply(d,e)
        self.assertEqual(f, [[19, 22], [43, 50]])

    def test_big_square(self):
        g = [[1,2,3],[4,5,6],[7,8,9]]
        h = [[4,5,6],[7,8,9],[1,2,3]]
        i = multiply(g,h)
        self.assertEqual(i, [[21,27,33],[57,72,87],[93,117,141]])

    def test_dimension_mismatch(self):
        j = [[1, 2, 3], [4, 5, 6]]
        k = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(Exception) as e:
            multiply(j,k)



if __name__ == '__main__':
    unittest.main()
