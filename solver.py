import copy, math
from itertools import *
from collections import defaultdict

class NoValueError(Exception): pass

def make_dict(startpuzzle):
    '''takes in a startpuzzle as a long string where zero reprsesents an unfilled sqare and a digit 1-9 is a value. Returns a dictionary where keys are coordinates and values are initial possible values for a square. For a square that already has a value this will make a list containing only that value, otherwise will make a list of [1..9]'''
    n = math.sqrt(len(startpuzzle))
    if n%1 != 0.0:
        raise ValueError('Your board is not square!')
    else:
        n = int(n)
    puzdict = defaultdict(set)

    for i in range(len(startpuzzle)):
        y = i // n
        x = i % n
        val = int(startpuzzle[i])
        if val == 0:
            puzdict[(y,x)] = set(range(1,n+1))
        else:
            puzdict[(y,x)].add(val)
    return puzdict


# we need to be able to pass down the size of our board, rather than hardcoding
# returns a dict and an integer, the size of the board

class Board_Accessor(object):
    @classmethod
    def get_square_val(cls, dict, y, x):
        """Returns the value of a square, if that square is solved
            (i.e. has only one possibility). Otherwise, returns None."""
        if len(dict[(y,x)]) == 1:
            return list(dict[(y,x)])[0]
        elif len(dict[(y,x)]) < 1:
            raise NoValueError("There are no possibilities for this square! You done fucked up.")
        else:
            return None

    #pass in n rather than using 9
    @classmethod
    def get_row(cls, dict, y):
        row = set()
        for i in range(9):
            val = cls.get_square_val(dict, y, i)
            if val:
                row.add(val)
        return row

    @classmethod
    def get_col(cls, dict, x):
        col = set()
        for i in range(9):
            val = cls.get_square_val(dict, i, x)
            if val:
                col.add(val)
        return col

    @classmethod
    def get_box(cls, dict, y, x):
        box = set()
        y_coords = [(y // 3) * 3 + i for i in range(3)]
        x_coords = [(x // 3) * 3 + i for i in range(3)]
        box_gen = product(y_coords,x_coords)
        for j,i in box_gen:
            val = cls.get_square_val(dict, j, i)
            if val:
                box.add(val)
        return box

    @classmethod
    def get_compare(cls, dict, y, x):
        compare = cls.get_row(dict, y) | cls.get_col(dict, x) | cls.get_box(dict, y, x)
        return compare

    @classmethod
    def is_solved(cls, dict):
        solved = True
        # if any values in dict are not lists of len 1, then sovled = False
        return solved

class Narrower(object):

    @classmethod
    def narrow_one(cls, dict, y, x, compare_func=Board_Accessor.get_compare):
        """Compares a given square to its row/col/box, narrows down
            possibilities, returns updated possibility set."""
        compare = compare_func(dict, y, x)
        return dict[(y,x)].difference(compare)

    @classmethod
    def narrow_all(cls, dict, compare_func=Board_Accessor.get_compare):
        for (y,x) in dict.keys():
            if len(dict[(y,x)]) > 1:
                dict[(y,x)] = cls.narrow_one(y,x,dict,compare_func)
        return dict

class Printer(object):
    pass

#pass functions instead of classes as args
def solve_dict(startpuzzle, dict_maker_func=make_dict, compare_func=Board_Accessor.get_compare, narrower=Narrower(), printer=Printer()):
    sudoku_dict, n = dict_maker_func(startpuzzle)

    while not board_accessor.is_solved(sudoku_dict):
        sudoku_dict = narrower.narrow_all(sudoku_dict, board_accessor)

    print "solved!\n"
    printer.render(sudoku_dict)


