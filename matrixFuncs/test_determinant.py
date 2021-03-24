from determinant import determinant
import unittest

class TestDeterminant(unittest.TestCase):

    def test_multi(self):
        a = [[1, 2], [4, 5]]
        b = determinant(a)
        self.assertEqual(b, -3)

    def test_3by3(self):
        c = [[1,2,3],[4,5,6],[7,8,9]]
        d = determinant(c)
        self.assertEqual(d, 0)

    def test_rectangle(self):
        e = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(Exception) as e:
            determinant(e)



if __name__ == '__main__':
    unittest.main()
