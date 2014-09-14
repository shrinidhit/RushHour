#!/usr/bin/env python

#
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#

#imports:
import numpy

#Global Variables:
GRID_SIZE = 6

#Classes

class block(object):
    """Encodes state of block"""
    def __init__(self, coordinate, direction):
        self.coordinate = coordinate
        self.size = size
        self.direction = direction

class car(block):
    """Encodes state of car: 2 units long"""
    def __init__(self, coordinate, direction):
        super(car, self).__init__()
        self.size = 2

class truck(block):
    """Encodes state of truck: 3 units long"""
    def __init__(self, coordinate, direction):
        super(truck, self).__init__()
        self.size = 3

class board(object):
    def __init__(self):
        self.blocks = []
        self.size = GRID_SIZE
    def add_block(self, block):
        self.blocks.append(block)
    def create_grid(self):
        self.grid = numpy.zeros(shape=(self.size, self.size))
    def update_grid(block):
        #Getting block position
        row_start, column_start = block.coordinate
        if block.direction == "h":
            row_end == row_start + block.size
        elif block.direction == "v":
            column_end == column_start + block_size
        else:
            fail("Invalid Block direction. Valid inputs: h for ""horizontal"" and v for ""vertical"")
        #Deleting block from old grid:
            for i in range(0, self.size):
                while block in grid[i]:
                    pass #Fix this
        #Creating new grid:
        for row in range(row_start, row_end):
            for column in range(column_start, column_end):
                self.grid[row, column] = block



# fail somewhat gracefully
def fail (msg):
    raise StandardError(msg)


def validate_move (brd,move):
    # FIX ME!
    # check that piece is on the board
    # check that piece placed so it can move in that direction
    # check that piece would be in bound
    # check that path to target position is free
    return False


def read_player_input (brd):
    # FIX ME!
    return None


def update_board (brd,move):
    # FIX ME!
    return brd


def print_board (brd):
    # FIX ME!
    print "<some output of the board>"

    
def done (brd):
    # FIX ME!
    return True


# initial board:
# Board positions (1-6,1-6), directions 'r' or 'd'
#
# X @ (2,3) r
# A @ (2,4) r
# B @ (2,5) d
# C @ (3,6) r
# O @ (4,3) d
# P @ (6,4) d


def create_initial_level ():
    # FIX ME!
    return None


def main ():

    brd = create_initial_level()

    print_board(brd)

    while not done(brd):
        move = read_player_input(brd)
        brd = update_board(brd,move)
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'
        

if __name__ == '__main__':
    #test
    testboard = board()
    testboard.create_grid()
    print testboard.grid
    print row
    print column

    # main()
