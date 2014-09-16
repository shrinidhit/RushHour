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

    def update_grid(self, block):

        #Getting block position
        row_start, column_start = block.coordinate
        row_start = row_start - 1;
        column_start = column_start - 1

        if block.direction == "r":
            row_end = row_start + block.size
            column_end = column_start + 1
        elif block.direction == "d":
            column_end = column_start + block.size
            row_end = row_start + 1
        else:
            fail ("Invalid Block direction. Valid inputs: r for ""right"" and d for ""down""")

        #Deleting block from old grid:
        for i in range(0, self.size):
            while block in self.grid[i]:
                loc = self.grid[i].index(block)
                self.grid[i][loc] = 0

        #Putting block in new position:
        for row in range(row_start, row_end):
            for column in range(column_start, column_end):
                if self.grid[column][row] == 0:
                    self.grid[column][row] = block
                else:
                    fail ("Blocks can not overlap")
    def add_block(self, block):
        # add new block to board.blocks list
        self.blocks.append(block)
        self.blocknames.append(block.name)
        self.update_grid(block)


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

def read_player_input (brd, move):
    blockname = move[0]
    direction = move[1]
    amount = move[2]

    #Checks if block is on board
    if blockname in brd.blocknames:
        block = name_to_object(brd, blockname)
    else: fail ("Block is not on board")

    #Checks if block can move in said direction
    if direction in ["u", "d"] and block.direction != "d":
        fail ("Invalid Block Direction")
    if direction in ["r", "l"] and block.direction != "r":
        fail ("Invalid Block Direction")

    #Gets new coordinates
    currentx, currenty = block.coordinate
    if direction == 'u': # up
        coordinate_new = (currentx, currenty + int(amount))
    elif direction == 'd': # down
        coordinate_new = (currentx, currenty - int(amount))
    elif direction == 'l': # left
        coordinate_new = (currentx + int(amount), currenty)
    elif direction == 'r': # right
        coordinate_new = (currentx - int(amount), currenty)

    #Checks if new coordinate is within boundries
    if 0 >= coordinate_new[0] or coordinate_new[0] >=5:
        fail ("Move not in bounds")

    #Checks if path to new coordinate is free:
    for x in range(currentx, coordinate_new[0] + 1):
        for y in range(currenty, coordinate_new[1] + 1):
            if grid[x][y] !=0:
                fail ("Move is blocked by another piece")

    return coordinate_new

def update_board (brd,move):
    # FIX ME!
    #Change coordinate of block in "move"
    #Update Board
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

    return True

def main ():

    brd = create_initial_level(level1)

    print_board(brd)

    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'

def test ():

    brd = create_initial_level(level1)
    print_board(brd)

if __name__ == '__main__':
    test()
    #main()
