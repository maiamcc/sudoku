import copy
from itertools import *
from collections import defaultdict

class NoValueError(Exception): pass

#make this just a function
class Dict_Init(object):

    def make_dict(startpuzzle):
        pass
    # we need to be able to pass down the size of our board, rather than hardcoding
    # returns a dict and an integer, the size of the board


    def get_square_val(self, dict, y, x):
        if len(dict[(y,x)]) == 1:
            return dict[(y,x)].pop()
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

    # to call: Board_Accessor.get_row()


    def get_col(self, dict, x):
        col = set()
        for i in range(9):
            val = self.get_square_val(dict, i, x)
            if val:
                col.add(val)
        return col

    def get_box(self, dict, y, x):
        box = set()
        y_coords = [(y // 3) * 3 + i for i in range(3)]
        x_coords = [(x // 3) * 3 + i for i in range(3)]
        box_gen = product(y_coords,x_coords)
        for j,i in box_gen:
            val = self.get_square_val(dict, j, i)
            if val:
                box.add(val)
        return box

    def is_solved(self, dict):
        solved = True
        # if any values in dict are not lists of len 1, then sovled = False
        return solved

class Narrower(object):
    def narrow_one(self, y, x, dict, board_accessor=Board_Accessor()):
        possibilities = set()
        return possibilities

    def narrow_all(self, dict, board_accessor=Board_Accessor()):
        for (y,x) in dict.keys():
            dict[(y,x)] = self.narrow_one(y,x,dict,board_accessor)
        return dict

class Printer(object):
    pass

#pass functions instead of classes as args
def solve_dict(startpuzzle, dict_initializer=Dict_Init(), board_accessor=Board_Accessor(), narrower=Narrower(), printer=Printer()):
    sudoku_dict, n = dict_initializer.make_dict(startpuzzle)

    while !board_accessor.is_solved(sudoku_dict):
        sudoku_dict = narrower.narrow_all(sudoku_dict, board_accessor)

    print "solved!\n"
    printer.render(sudoku_dict)


