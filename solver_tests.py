import unittest
from solver import Board_Accessor, NoValueError
import random

class getSquareValReturnsValIfSquareSolved(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(1,1): [5]}
        self.Board_Accessor = Board_Accessor()

    def runTest(self):
        val = self.Board_Accessor.get_square_val(self.mockDict, 1, 1)
        self.assertTrue(val == 5)

class getSquareValReturnsNoneIfSquareNotSolved(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(1,1): [1, 2, 3, 4, 5]}
        self.Board_Accessor = Board_Accessor()

    def runTest(self):
        val = self.Board_Accessor.get_square_val(self.mockDict, 1, 1)
        self.assertIsNone(val)

class getSquareValThrowsErrorIfNoPossibilities(unittest.TestCase):
    def setUp(self):
        self.mockDict = {(1,1): []}
        self.Board_Accessor = Board_Accessor()

    def runTest(self):
        self.assertRaises(NoValueError, self.Board_Accessor.get_square_val, self.mockDict, 1, 1)

if __name__ == '__main__':
    unittest.main()