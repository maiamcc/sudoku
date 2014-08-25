import copy
def draw_board(board):
    copyboard = copy.deepcopy(board)
    for i in range(0,9):
        copyboard[i].insert(6, "|")
        copyboard[i].insert(3, "|")
        row_string = "  ".join(map(str, copyboard[i]))
        if i in [2, 5]:
            print row_string
            print "________________________________"
        else:
            print row_string

def newboard():
    return [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]