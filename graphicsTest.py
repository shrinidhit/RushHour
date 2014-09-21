from graphics import *
from rush import level1
from rush import block
from rush import car
from rush import truck

win = GraphWin("graphicsTest", 600, 600) # names & sizes window (pixels)
win.setCoords( 0, 8, 8, 0 ) # makes coordinates un-ugly (the rectangle in (row1, column1) will have its top left-hand corner in (1,1), rectangle in (row3, column5) will have (3,5), etc.)
pieceMap = {}


def create_board():
    coordMap =  {} # dictionary of coordinate pairs mapping to respective rectangles
    
    # marks exit/goal w/ red line
    ln = Line(Point(7,3), Point(7,4))
    ln.setOutline('red')
    ln.setWidth(5)
    ln.draw(win)
        
    # draws empty rectangles/board
    for i in range(1,7):
        for j in range(1,7):
            coord = (i,j) # coord of rectangle's top left-hand corner
            rect = Rectangle(Point(i,j), Point(i+1,j+1))
            coordMap[coord] = rect # ads coord:rect to dictionary (yay!)
            rect.draw(win)
    # print coordMap ##### Wooohoooooooooooooo!!!! #####
    # win.getMouse() # Pause to view result
    # win.close()    # Close window when done

def display_object(block):
    spaces = block.size
    topLefty, topLeftx = block.coordinate
    if block.direction == 'd':
        piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+1,topLefty+spaces))
        pieceMap[block.coordinate] = piece
    elif block.direction == 'r':
        piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+spaces,topLefty+1))
    piece.setFill('red')
    piece.setOutline('white')
    piece.setWidth(2)
    piece.draw(win)


    # for i in range(0, len(locs), 4):

    #     if locPiece[0] in ('X','A','B','C'):
    #         piece = block()
    #     elif locPiece[0] in ('P','Q','R','S'):
    #         spaces = 3
    #     if locPiece[3] == 'd':
    #         piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+1,topLefty+spaces))
    #         pieceMap[coord] = piece
    #     elif locPiece[3] == 'r':
    #         piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+spaces,topLefty+1))
    #         pieceMap[coord] = piece
    #     print pieceMap
    #     piece.setFill('red')
    #     piece.setOutline('white')
    #     piece.setWidth(2)
    #     piece.draw(win)


    # pieceMap


    # piece = rectCoord[(2,3)] # example of how we would locate and draw a car/truck object
    # piece.setFill('red')


    win.getMouse() # Pause to view result
    win.close()    # Close window when done
        

car1 = car('A', (2,2), 'd')
create_board()
display_object(car1)