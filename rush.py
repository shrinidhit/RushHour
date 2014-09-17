#!/usr/bin/env python

# Shrinidhi Thirumalai and Allison Patterson
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#

#Global Variables:
GRID_SIZE = 6
level1 = "A21dB31rC51dD61dE42dF63dI34rH45dX23r" # initial coordinates of each block object (yikes!)

#Classes

class block(object):
    """Encodes state of block"""
    def __init__(self, name, coordinate, direction):
        self.name = name #name of block
        self.coordinate = coordinate # tuple
        self.direction = direction # orientation of block

class car(block):
    """Encodes state of car: 2 units long"""
    def __init__(self, name, coordinate, direction):
        super(car, self).__init__(name, coordinate, direction)
        self.size = 2

class truck(block):
    """Encodes state of truck: 3 units long"""
    def __init__(self, name, coordinate, direction):
        super(truck, self).__init__(name, coordinate, direction)
        self.size = 3

class board(object):
    def __init__(self):
        self.blocks = [] # create empty list of blocks on board, and empty grid
        self.blocknames = []
        self.size = GRID_SIZE
        self.grid = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]

        # row = []
        # for i in range(0, GRID_SIZE):
        #     row.append(0)
        # for i in range(0, GRID_SIZE):
        #     self.grid.append(row)
    def add_block(self, block):
        # add new block to board.blocks list
        self.blocks.append(block)
        self.blocknames.append(block.name)
        self.update_grid(block)
    def grid_object(self, row, column):
        return self.grid[row - 1][column -1]
    def grid_assign(self, row, colunm, newitem):
        self.grid[row - 1][colunm - 1] = newitem

    def update_grid(self, block):

        #Getting block position
        row_start, column_start = block.coordinate
        row_start = row_start
        column_start = column_start

        if block.direction == "r":
            row_end = row_start + block.size
            column_end = column_start + 1
        elif block.direction == "d":
            column_end = column_start + block.size
            row_end = row_start + 1
        else:
            fail ("Invalid Block direction. Valid inputs: r for ""right"" and d for ""down""")

        #Deleting block from old grid:
        for i in range(1, self.size + 1):
            while block in self.grid[i]:
                loc = self.grid[i].index(block) + 1
                self.brd.grid_assign(i, loc, 0)

        #Putting block in new position:
        for row in range(row_start, row_end):
            for column in range(column_start, column_end):
                if self.grid_object(row,column) == 0:
                    self.grid_assign(row,column, block)
                else:
                    fail ("Blocks can not overlap")


# fail somewhat gracefully
def fail (msg):
    raise StandardError(msg)

def name_to_object(brd, objectName):
    index = brd.blocknames.index(objectName)
    return brd.blocks[index]

def string_to_new_object(object_string):
    name = object_string[0]
    coordinate = (int(object_string[1]), int(object_string[2]))
    direction = object_string[3]
    if name in ["X", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]:
        return car(name, coordinate, direction)
    elif name in ["O", "P", "Q", "R"]:
        return truck(name, coordinate, direction)
    else:
        fail ("invalid car naming")

def create_initial_level (level_string):
    # FIX ME!
    # initial board:
    # Board positions (1-6,1-6), directions 'r' or 'd'

    start_board = board()
    for i in range(0, len(level_string), 4):
        object_string = level_string[i:i+4]
        start_board.add_block(string_to_new_object(object_string))
    return start_board

def get_player_input():
    move=raw_input('Enter your move(example: Au2) :')
    return move

def read_player_input (brd, move):
    blockname = move[0]
    direction = move[1]
    amount = int(move[2])

    #Checks if block is on board
    if blockname in brd.blocknames:
        block = name_to_object(brd, blockname)
    elif blockname.upper() in brd.blocknames:
        blockname = blockname.upper()
        block = name_to_object(brd, blockname)
    else: fail ("Block is not on board")

    #Checks if block can move in said direction
    if direction in ["u", "d"] and block.direction != "d":
        fail ("Invalid Block Direction")
    if direction in ["r", "l"] and block.direction != "r":
        fail ("Invalid Block Direction")

    #Gets new coordinates
    currentx, currenty = block.coordinate
    print block.coordinate
    if direction == 'u': # up
        coordinate_new = (currentx, currenty - int(amount))
    elif direction == 'd': # down
        coordinate_new = (currentx, currenty + int(amount))
    elif direction == 'l': # left
        coordinate_new = (currentx - int(amount), currenty)
    elif direction == 'r': # right
        coordinate_new = (currentx + int(amount), currenty)

    #Checks if new coordinate is within boundries
    if 1 > coordinate_new[0] or coordinate_new[0] > 6:
        fail ("Move not in bounds")

    #Checks if path to new coordinate is free:
    for x in range(currentx, coordinate_new[0] + 1):
        for y in range(currenty, coordinate_new[1] + 1):
            if brd.grid_object(x,y) !=0 and brd.grid_object(x,y) != brd.grid_object(currentx, currenty):
                fail ("Move is blocked by another piece")

    return [blockname, coordinate_new]

def update_board (brd, blockname, coordinate_new):
    block = name_to_object(brd, blockname)
    block.coordinate = coordinate_new
    brd.update_grid(block)
    return brd

def print_board (brd):
    # FIX ME!
    brd = brd.grid
    for row in brd:
        for car in row:
            if car == 0:
                print "_",
            else:
                print car.name,
        print ""
    print "" ##### do we need this line? ##### <-----Yup, it adds an empty space after the whole grid is printed.
    
def done (brd):
    #Check if object X's coordinate is at end position. Return True if it is
    endpoint1 = brd.grid_object(3,5)
    endpoint2 = brd.grid_object(3,6)

    if type(endpoint1) is block:
        if endpoint1.name == 'X': return True
    elif type(endpoint2) is block:
        if endpoint2.name == 'X': return True
    return False

def main ():

    brd = create_initial_level(level1)

    print_board(brd)

    while not done(brd):
        playerinput = get_player_input()
        move = read_player_input(brd, playerinput)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'

def test ():
    brd = create_initial_level(level1)

    print_board(brd)

    while not done(brd):
        moveString = get_player_input()
        move = read_player_input(brd, moveString)
        brd = update_board(brd, move[0], move[1])
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'

if __name__ == '__main__':
    test()
    #main()
