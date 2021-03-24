from subtract import subtract
import unittest

class TestSubtract(unittest.TestCase):

    def test_2by2(self):
        a = [[1, 2], [4, 5]]
        b = [[1, 2], [3, 4]]
        c = subtract(a, b)
        self.assertEqual(c, [[0, 0], [1, 1]])
        
    def test_3by3(self):
        a = [[1,2,3],[4,5,6],[7,8,9]]
        b = [[1,2,3],[6,5,4],[9,8,7]]
        c = subtract(a, b)
        self.assertEqual(c, [[0,0,0],[-2,0,2],[-2,0,2]])
        
    def test_rectange(self):
        a = [[1, 2], [4, 5],[7,6]]
        b = [[1, 2], [3, 4],[6,7]]
        c = subtract(a, b)
        self.assertEqual(c, [[0, 0], [1, 1],[1,-1]])
        


if __name__ == '__main__':
    unittest.main()
