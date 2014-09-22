# Shrinidhi Thirumalai and Allison Patterson
# Game Programming, Level 1 Project
#
# RUSH HOUR
#
# A simple puzzle game, based on the physical game of the same name 
# by Binary Arts Corp
#

#Global Variables:
#from graphicsTest import * ##### I put the thingy at the bottom #####

#Imports
from graphics import *

#Global Variables
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
    """Encodes state of board as a six by six grid. Zeros represent no block.
    When a block is present, it is put into it's corresponding grid spot as (row, column)"""
    def __init__(self):
        self.blocks = [] #list of block objects
        self.blocknames = [] #list of block names strings
        self.size = GRID_SIZE
        #Initializing Grid:
        self.grid = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]

    def add_block(self, block):
        """add new block to board.blocks list"""
        self.blocks.append(block)
        self.blocknames.append(block.name)
        self.update_grid(block)

    def grid_object(self, row, column):
        """Returns the object in a given grid row and column"""
        return self.grid [row - 1][column -1]

    def grid_assign(self, row, column, newitem):
        """Places given item into grid at given row and column"""
        self.grid[row - 1][column - 1] = newitem

    def update_grid(self, block):
        """Updates a given block in the grid"""
        #extracting some useful attribute information
        row_start, column_start = block.coordinate
        row_start = row_start
        column_start = column_start

        if block.direction == "d":
            row_end = row_start + block.size
            column_end = column_start + 1
        elif block.direction == "r":
            column_end = column_start + block.size
            row_end = row_start + 1
        else:
            fail ("Invalid Block direction. Valid inputs: r for ""right"" and d for ""down""")

        #Deleting block from old grid:
        for i in range(0, self.size):
            while block in self.grid[i]:
                loc = self.grid[i].index(block) + 1
                self.grid_assign(i + 1, loc, 0)

        #Putting block in new position:
        for row in range(row_start, row_end):
            for column in range(column_start, column_end):
                if self.grid_object(row,column) == 0:
                    self.grid_assign(row,column, block)
                else:
                    fail ("Blocks can not overlap")

class Display(object):
    """Class containing methods to group the pretty display for Game, using the graphics.py framework"""

    def __init__(self):
        """Displays an empty six by six grid"""
        # Initializations of Attributes:
        self.pieceMap = {} #dictionary of 
        self.coordMap =  {} # dictionary of coordinate pairs mapping to respective rectangles
        self.rectangles = []
        self.win = GraphWin("graphicsTest", 600, 600) # names & sizes window (pixels)
        self.win.setCoords( 0, 8, 8, 0 ) # makes coordinates un-ugly (the rectangle in (row1, column1) will have its top left-hand corner in (1,1), rectangle in (row3, column5) will have (3,5), etc.)
        self.selected = [1,1]
        self.highlight = Rectangle(Point(self.selected[0],self.selected[1]), Point(self.selected[0] + 1,self.selected[1] + 1))
        self.highlight.draw(self.win)
        
        # marks exit/goal w/ red line
        ln = Line(Point(7,3), Point(7,4))
        ln.setOutline('red')
        ln.setWidth(5)
        ln.draw(self.win)
            
        # draws empty rectangles/board
        for i in range(1,7):
            for j in range(1,7):
                coord = (i,j) # coord of rectangle's top left-hand corner
                rect = Rectangle(Point(i,j), Point(i+1,j+1))
                self.coordMap[coord] = rect # ads coord:rect to dictionary (yay!)
                rect.draw(self.win)


    def display_object(self, block):
        """Displays a given block object on the Screen"""
        self.pieceMap[block.coordinate] = block
        spaces = block.size
        topLefty, topLeftx = block.coordinate
        #Direction
        if block.direction == 'd':
            piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+1,topLefty+spaces))
        elif block.direction == 'r':
            piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+spaces,topLefty+1))
        #Color
        if block.name == 'X':
            piece.setFill('red')
        elif block.size == 2:
            piece.setFill('blue')
        else:
            piece.setFill('green')
        piece.setOutline('white')
        piece.setWidth(2)
        piece.draw(self.win)
        self.rectangles.append(piece)

    def update_blocks(self, board):
        """Refreshes the pieceMap dictionary and refreshes the screen"""
        blocklist = board.blocks
        self.pieceMap = {}
        for block in blocklist:
            self.pieceMap[block.coordinate] = block

    def show_highlight(self):
        """Highlights a box when it is clicked, showing that it is selected"""
        self.highlight.undraw()
        self.highlight = Rectangle(Point(self.selected[0],self.selected[1]), Point(self.selected[0] + 1,self.selected[1] + 1))
        self.highlight.draw(self.win)
        self.highlight.setOutline('black')
        self.highlight.setWidth(5)

    def print_display(self, board):
        """Main Display loop for every refreshment. 
        Erases the old board, updates the blocks, then draws a new one"""
        for rect in self.rectangles:
            rect.undraw()
        self.update_blocks(board)
        for block in board.blocks:
            self.display_object(block)
        self.highlight.undraw()

    def extract_coord(self, point):
        """Extracts and returns a tuple of coordinates when 
        given a point object(a class from the graphics.py library)"""
        x = point.getX()
        y = point.getY()
        xindex = int(x)#rounds value
        yindex = int(y)
        return (xindex, yindex)

    def click_to_block(self, point, board):
        """Returns the block or board piece under an inputted point from a click"""
        #Getting indexes
        index = self.extract_coord(point)
        column, row = index
        #Selecting piece
        piece = self.coordMap[index]
        self.selected = [column, row]
        if type(board.grid_object(row, column)) != int:
            block = board.grid_object(row, column)
            return block

    def when_clicked(self, point, board):
        """Main sequence run from the input of a board piece click. The block under the click is found,
        the square is highlighted, then the block is returned """
        block = self.click_to_block(point, board)
        self.show_highlight()
        return block

# fail somewhat gracefully
def get_next_click(Display):
    """Extracts the coordinates of the board on which the second click was made"""
    secondclick = Display.win.getMouse()
    #Getting indexes
    index = Display.extract_coord(secondclick)
    column, row = index
    #Selecting piece
    piece = Display.coordMap[index]
    Display.selected = [column, row]
    return index

def click_to_move(brd, Display, point):
    """Full sequence for getting user input. The first click is made and used to get the block object,
    then the second one is made to get directional input. This is returned as a list of blockname,
    direction, and amount to move"""
    #extracts name
    block = Display.click_to_block(point, brd)
    blockname = block.name
    column, row = Display.extract_coord(point)
    secondindex = get_next_click(Display)
    #extracts direction and amount
    endcolumn, endrow = secondindex
    if column == endcolumn and endrow > row:
        direction = 'd'
        amount = endrow - row
    elif column == endcolumn and endrow < row:
        direction = 'u'
        amount = row - endrow
    elif row == endrow and endcolumn > column:
        direction = 'r'
        amount = endcolumn - column
    elif row == endrow and endcolumn < column:
        direction = 'l'
        amount = column - endcolumn
    else:
        fail('invalid direction')
    #returns list representing move
    return [blockname, direction, amount]

def fail (msg):
    """Message to User when something in the game goes wrong"""
    raise StandardError(msg)

def name_to_object(brd, objectName):
    """Outputs an actual block object when inputted a string of it's name"""
    index = brd.blocknames.index(objectName)
    return brd.blocks[index]

def string_to_new_object(object_string):
    """Creates a new string object when given a string representing it's name, direction, and coordinate
    in the form X23d"""
    name = object_string[0]
    coordinate = (int(object_string[2]), int(object_string[1]))
    direction = object_string[3]
    if name in ["X", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]:
        return car(name, coordinate, direction)
    elif name in ["O", "P", "Q", "R"]:
        return truck(name, coordinate, direction)
    else:
        fail ("invalid car naming")

def create_initial_level (level_string):
    """Creates the starting board sequence when given a level as a long string"""
    start_board = board()
    for i in range(0, len(level_string), 4):
        object_string = level_string[i:i+4]
        start_board.add_block(string_to_new_object(object_string))
    return start_board

def get_player_input():
    """First iteration technique of getting user input as a string of 3 letter/numbers
    such as Au2(move piece A up by 2 squares)"""
    move=raw_input('Enter your move(example: Au2) :')
    return move

def string_to_move(string):
    """Outputs a list representing a move [blockname, direction, amount] when 
    input a user string representing the move"""
    blockname = string[0]
    direction = string[1]
    amount = int(string[2])
    return [blockname, direction, amount]

def read_player_input (brd, move):
    """Takes in a list representing motion[blockname, direction, amount] and
    returns the blockname and it's new coordinate after the move if 
    it is valid. Else, throws error"""

    move = string_to_move(move)
    blockname = move[0]
    direction = move[1]
    amount = move[2]

    #Checks if block is on board
    if blockname in brd.blocknames:
        block = name_to_object(brd, blockname)
    elif blockname.upper() in brd.blocknames:
        blockname = blockname.upper()
        block = name_to_object(brd, blockname)
    else: fail ("Block is not on board")

    #Checks if block can move in said direction
    if direction in ["u", "d"] and block.direction == "r":
        fail ("Invalid Block Direction")
    if direction in ["r", "l"] and block.direction == "d":
        fail ("Invalid Block Direction")

    #Gets new coordinates
    currentx, currenty = block.coordinate
    if direction == 'u': # up
        coordinate_new = (currentx - int(amount), currenty)
        coordinate_end = (coordinate_new[0] + 1, coordinate_new[1])
    elif direction == 'd': # down
        coordinate_new = (currentx + int(amount), currenty)
        coordinate_end = (coordinate_new[0] + 1, coordinate_new[1])
    elif direction == 'l': # left
        coordinate_new = (currentx, currenty - int(amount))
        coordinate_end = (coordinate_new[0], coordinate_new[1] + 1)
    elif direction == 'r': # right
        coordinate_new = (currentx, currenty + int(amount))
        coordinate_end = (coordinate_new[0], coordinate_new[1] + 1)

    #Checks if new coordinate is within boundries
    if coordinate_new[0] < 1 or coordinate_new[0] > 6 or coordinate_end[0] < 1 or coordinate_end[0] > 6:
        fail ("Move not in bounds")
    if coordinate_new[1] < 1 or coordinate_new[1] > 6 or coordinate_end[1] < 1 or coordinate_end[1] > 6:
        fail ("Move not in bounds")

    #Checks if path to new coordinate is free:
    for x in range(currentx, coordinate_new[0] + 1):
        for y in range(currenty, coordinate_new[1] + 1):
            if brd.grid_object(x,y) !=0 and brd.grid_object(x,y) != brd.grid_object(currentx, currenty):
                fail ("Move is blocked by another piece")

    return [blockname, coordinate_new]
    

def update_board (brd, blockname, coordinate_new):
    """Given a blockname and it's new coordinate, this updates the board and grid"""
    block = name_to_object(brd, blockname)
    block.coordinate = coordinate_new
    brd.update_grid(block)
    return brd

def print_board (brd):
    """Prints board to console"""
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
    """Check if object X's coordinate is at end position. Return True if it is"""
    endpoint = brd.grid_object(3,6)
    if type(endpoint) is car:
        if endpoint.name == 'X': return True
    return False

def main ():
    """Main game loop - default level"""
    brd = create_initial_level(level1)

    print_board(brd)

    while not done(brd):
        playerinput = get_player_input()
        move = read_player_input(brd, playerinput)
        brd = update_board(brd,move[0], move[1])
        print_board(brd)

    print 'YOU WIN! (Yay...)\n'

def main_with_initial(level):
    """Main game loop with level input as a string"""
    brd = create_initial_level(level)

    print_board(brd)

    while not done(brd):
        playerinput = get_player_input()
        move = read_player_input(brd, playerinput)
        brd = update_board(brd,move[0], move[1])
        print_board(brd)
    print 'YOU WIN! (Yay...)\n'



if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        main_with_initial (sys.argv[1])
    else:
        main()
