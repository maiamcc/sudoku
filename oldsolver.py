import copy
from itertools import *
from collections import defaultdict

def newboard():
    return [[0,0,0,0,8,9,0,0,0],
        [9,0,1,0,4,0,7,0,0],
        [8,0,0,5,0,2,0,0,3],
        [6,0,0,1,0,0,4,0,8],
        [5,7,0,0,0,4,0,3,0],
        [0,0,0,0,0,0,2,5,0],
        [4,0,6,2,5,0,8,0,9],
        [2,0,0,0,0,0,0,0,0],
        [7,9,0,6,0,8,0,2,4]]

# constructor - only assignment

class Board(list):
    def __init__(self, startboard):
        super(Board, self).__init__(startboard)
        self.n = self.__len__()
        self.empties = get_empties(self)
        self.square_dict = make_square_dict(self)

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

def make_square_dict(board):
    temp_dict = defaultdict(list)
    for y in range(3):
        for x in range(3):
            y_coords = [y * 3 + i for i in range(3)]
            x_coords = [x * 3 + i for i in range(3)]
            square_gen = product(y_coords,x_coords)
            for j,i in square_gen:
                temp_dict[(y,x)].append((j,i))
    return temp_dict

#board accessor class
def get_row(board, y):
    return set(board[y])

def get_col(board, x):
    col = []
    for row in board:
        col.append(row[x])
    return set(col)

def get_square(board, y, x):
    # combine with square dict
    square_vals = set()
    square_y = y // 3
    square_x = x // 3
    square_points = board.square_dict[(square_y,square_x)]
    for j,i in square_points:
        square_vals.add(board[j][i])
    return square_vals

def get_empties(board):
    # populate dictionary with possible values for all empty squares
    temp_dict = {}
    for y in range(board.n):
        for x in range(board.n):
            if board[y][x] == 0:
                temp_dict[(y,x)] = set(i for i in range(1,10))
    return temp_dict

def get_compare(board, y, x):
    compare = get_row(board, y) | get_col(board, x) | get_square(board, y, x)
    compare.remove(0)
    return compare

def narrow(board, y, x):
    compare = get_compare(board, y, x)
    board.empties[(y,x)] = board.empties[(y,x)].difference(compare)

    # if there's only value in the dict., that's the answer:
        # put answer in board, remove point from 'empties' dict
    if len(board.empties[(y,x)]) == 1:
        board[y][x] = board.empties[(y,x)].pop()
        board.empties.pop((y,x))

# @ static method??
# instance method passed 'self'... class method is not passed 'self' b/c doens't rely on an instance
# we want instance methods... b/c can mock it out. MockBoard.doathing = "what i want you to return"


def narrow_all(board):
    for key in board.empties.keys():
        narrow(board, key[0], key[1])

# optimization: only narrow squares in reach of those recently changed?

def solve_all(board, dictinit=dictionary_initializer):
    while board.empties.keys():
        narrow_all(board)
    return board