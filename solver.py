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
    return puzdict, n


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
        for val in dict.values():
            if len(val) > 1:
                solved = False
                break
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
                dict[(y,x)] = cls.narrow_one(dict, y, x, compare_func)
        return dict

def render(dict):
    for i in range(9):
        if i%3 == 0 and i != 0:
            print "________________________________"
        row = []
        for j in range(9):
            if j%3 == 0 and j != 0:
                row.append("|")
            if len(dict[(i,j)]) == 1:
                val = list(dict[(i,j)])[0]
            else:
                val = 0
            row.append(str(val))
        print "  ".join(row)

#pass functions instead of classes as args
def solve_dict(startpuzzle, dict_maker_func=make_dict, compare_func=Board_Accessor.get_compare, narrower_func=Narrower.narrow_all, printer=render):
    sudoku_dict, n = dict_maker_func(startpuzzle)

    while not Board_Accessor.is_solved(sudoku_dict):
        sudoku_dict = narrower_func(sudoku_dict, compare_func)

    print "solved!\n"
    printer(sudoku_dict)


