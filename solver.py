import copy
from itertools import *
from collections import defaultdict

class NoValueError(Exception): pass

class Dict_Init(object):

    def make_dict(startpuzzle):
        pass

class Board_Accessor(object):
    def get_square_val(self, dict, y, x):
        if len(dict[(y,x)]) == 1:
            return dict[(y,x)][0]
        elif len(dict[(y,x)]) < 1:
            raise NoValueError("There are no possibilities for this square! You done fucked up.")
        else:
            return None

    def get_row(self, dict, y):
        row = set()
        for i in range(9):
            val = get_square_val(dict, y, i)
            if val:
                row.add(val)
        return row

    def get_col(self, dict, x):
        col = set()
        for i in range(9):
            val = get_square_val(dict, i, x)
            if val:
                col.add(val)
        return col

    def get_box(self, dict, y, x):
        box = set()
        y_coords = [(y // 3) * 3 + i for i in range(3)]
        x_coords = [(x // 3) * 3 + i for i in range(3)]
        box_gen = product(y_coords,x_coords)
        box_points = board.box_dict[(box_y,box_x)]
        for j,i in box_gen:
            val = get_square_val(dict, j, i)
            if val:
                box.add(val)
        return box

class Narrower(object):
    pass

class Printer(object):
    pass


def solve_dict(startpuzzle, dict_initializer=Dict_Init(), board_accessor=Board_Accessor(), narrower=Narrower(), printer=Printer()):
    pass