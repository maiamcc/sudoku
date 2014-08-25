import copy
from itertools import *
from collections import defaultdict

def draw_board(board):
    for i in range(0,9):
        this_row = board[i][:]
        this_row.insert(6, "|")
        this_row.insert(3, "|")
        # vert_divide = "    |    |    |"
        row_string = "  ".join(map(str, this_row))
        if i in [2, 5]:
            print row_string
            print "________________________________"
        else:
            print row_string

def newboard():
    return [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,2,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]



class Board(list):
    def __init__(self, startboard):
        super(Board, self).__init__(startboard)
        self.empty = self.getempties()
        self.n = 9
        self.square_dict = self.make_square_dict()

    def __str__(self):
        print_str = ""
        for i in range(0, len(self)):
            this_row = copy.deepcopy(self[i])
            this_row.insert(6, "|")
            this_row.insert(3, "|")
            row_string = ("  ".join(map(str, this_row)) + "\n")
            if i in [2, 5]:
                print_str += (row_string)
                print_str += ("________________________________\n")
            else:
                print_str += (row_string)
        return print_str

    def make_square_dict(self):
        temp_dict = defaultdict(list)
        for y in range(3):
            for x in range(3):
                y_coords = [y * 3 + i for i in range(3)]
                x_coords = [x * 3 + i for i in range(3)]
                square_gen = product(y_coords,x_coords)
                for j,i in square_gen:
                    temp_dict[(y,x)].append((j,i))
        return temp_dict
    #note, do we really need this?
    def get_row(self,y):
        return set(self[y])

    def get_col(self,x):
        col = []
        for row in self:
            col.append(row[x])
        return set(col)

    def get_square(self, y, x):
        square_vals = set()
        square_y = y // 3
        square_x = x // 3
        square_points = self.square_dict((square_y,square_x))
        for j,i in square_points:
            square_vals.add(self[j][i])
        

    def getempties(self):
        # populate dictionary with possible values for all empty squares
        temp_dict = {}
        for y in range(self.__len__()):
            for x in range(self.__len__()):
                if self[y][x] == 0:
                    temp_dict[(y,x)] = set(i for i in range(1,10))
        return temp_dict

    def get_compare((y,x)):
        compare = get_row(y) | get_col(x) | get_square(y,x)
        compare.remove(0)
        return compare

    def narrow((y,x)):
        compare = get_compare((y,x))

    def narrow_all():
        for key in self.empty.keys():
            narrow(key)

    def solve_all():
        while self.empty.keys():
            narrow_all()
        return "solved!"




    # empty = [list of squares]