import unittest
from solver import *
import random

class boardConstructorMakesBoard(unittest.TestCase):
    def setUp(self):
        self.mockBoard = [[random.randint(0,10) for i in range(9)] for j in range(9)]

    def runTest(self):
        myboard = Board(self.mockBoard)
        self.assertTrue(len(myboard) == 9 & len(myboard[0]) == 9)
        """List of lists
        all elements are ints
        .n = 9
        .empties =
        .squarevals =
        """

class getEmptiesMakesEmptyDictIfNoEmpties(unittest.TestCase):
    def setUp(self):
        self.mockBoard = [[random.randint(1,10) for i in range(9)] for j in range(9)]
        self.mockBoard.n = 9

    def runTest(self):
        empties = get_empties(mockBoard)
        assert

class getEmptiesMakesDictOfEmpties(unittest.TestCase):
    def setUp(self):
        self.mockBoard = [[random.randint(1,10) for i in range(9)] for j in range(9)]

if __name__ == '__main__':
    unittest.main()