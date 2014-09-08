import unittest
from solver import Board_Accessor,NoValueError,make_dict
import random

class getSquareValReturnsValIfSquareSolved(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(1,1):set([5])}

    def runTest(self):
        val = Board_Accessor.get_square_val(self.mockDict,1,1)
        self.assertEqual(val,5)

class getSquareValReturnsNoneIfSquareNotSolved(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(1,1):set([1,2,3,4,5])}

    def runTest(self):
        val = Board_Accessor.get_square_val(self.mockDict,1,1)
        self.assertIsNone(val)

class getSquareValThrowsErrorIfNoPossibilities(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(1,1):set([])}

    def runTest(self):
        self.assertRaises(NoValueError,Board_Accessor.get_square_val,self.mockDict,1,1)

class getRowReturnsValuesInRow(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(0,0):set([5]),(0,1):set([1,2,3]),(0,2):set([4]),(0,3):set([8]),(0,4):set([1,2,3,6]),(0,5):set([6,7,9]),(0,6):set([7,9]),(0,7):set([1,2,6]),(0,8):set([6,7]),(1,0):set([1]),(1,1):set([1])}

    def runTest(self):
        row = Board_Accessor.get_row(self.mockDict,0)
        self.assertEqual(row,set([4,5,8]))

class getColReturnsValuesInCol(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(0,0):set([5]),(1,0):set([1,2,3]),(2,0):set([4]),(3,0):set([8]),(4,0):set([1,2,3,6]),(5,0):set([6,7,9]),(6,0):set([7,9]),(7,0):set([1,2,6]),(8,0):set([6,7]),(0,1):set([1]),(1,1):set([1])}

    def runTest(self):
        col = Board_Accessor.get_col(self.mockDict,0)
        self.assertEqual(col,set([4,5,8]))

class getBoxReturnsValuesInSquare(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(0,0):set([5]),(0,1):set([1,2,3]),(0,2):set([4]),(1,0):set([8]),(1,1):set([1,2,3,6]),(1,2):set([6,7,9]),(2,0):set([7,9]),(2,1):set([1,2,6]),(2,2):set([6,7]),(5,0):set([5]),(5,1):set([1]),(5,2):set([4]),(5,3):set([8]),(5,4):set([1]),(5,5):set([6,7,9]),(5,6):set([7,9]),(5,7):set([1,2,6]),(5,8):set([6,7]),(0,3):set([1]),(0,4):set([1])}

    def runTest(self):
        box = Board_Accessor.get_box(self.mockDict,2,2)
        self.assertEqual(box,set([4,5,8]))

class makeDictMakesCorrectDict(unittest.TestCase):
    def runTest(self):
        self.assertEqual(make_dict('0011'),{(0,0):set([1,2]),(0,1):set([1,2]),(1,0):set([1]),(1,1):set([1])})

class makeDictErrorsOnNotSquare(unittest.TestCase):
    def runTest(self):
        self.assertRaises(ValueError,make_dict,'000000')


class getCompareReturnsComparisonSet(unittest.TestCase):
    def setUp(self):
        self.mockDict = make_dict('000089000901040700800502003600100408570004030000000250406250809200000000790608024')
    def runTest(self):
        compare = Board_Accessor.get_compare(self.mockDict,0,0)
        self.assertEqual(compare,set([1,2,4,5,6,7,8,9]))

if __name__ == '__main__':
    unittest.main()