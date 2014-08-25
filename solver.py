import copy

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

class Box(object):

    '''
    solved = False
    value = "x"
    choices = [1,2,3,4,5,6]
    x = ?
    y = ?

    # if it's in progress, value = 0
    def __str__(self):
        return self.value

    def __repr__(self):
        return "Box at (%s,%s); value = %s; choices = %s" % (self.x, self.y, self.value, self.choices)
    '''

class Board(list):
    def __init__(self, startboard):
        super(Board, self).__init__(startboard)

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

    # empty = [list of squares]