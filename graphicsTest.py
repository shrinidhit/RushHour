from graphics import *

def create_board():
    rectCoord =  {} # dictionary of coordinate pairs mapping to respective rectangles
    win = GraphWin("graphicsTest", 600, 600) # names & sizes window (pixels)
    win.setCoords( 0, 8, 8, 0 ) # makes coordinates un-ugly (the rectangle in (row1, column1) will have its top left-hand corner in (1,1), rectangle in (row3, column5) will have (3,5), etc.)
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
            rectCoord[coord] = rect # ads coord:rect to dictionary (yay!)
            rect.draw(win)
    # print rectCoord ##### Wooohoooooooooooooo!!!! #####

    piece = rectCoord[(2,3)] # example of how we would locate and draw a car/truck object
    piece.setFill('red')


    win.getMouse() # Pause to view result
    win.close()    # Close window when done
        



create_board()