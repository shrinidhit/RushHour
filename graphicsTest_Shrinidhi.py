from graphics import *
from rush import block
from rush import car
from rush import truck

class Display(object):
    """docstring for Display"""
    def __init__(self):
        # Initializations of Attributes:
        self.pieceMap = {} #dictionary of 
        self.coordMap =  {} # dictionary of coordinate pairs mapping to respective rectangles
        self.win = GraphWin("graphicsTest", 600, 600) # names & sizes window (pixels)
        self.win.setCoords( 0, 8, 8, 0 ) # makes coordinates un-ugly (the rectangle in (row1, column1) will have its top left-hand corner in (1,1), rectangle in (row3, column5) will have (3,5), etc.)
        
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
        spaces = block.size
        topLefty, topLeftx = block.coordinate
        if block.direction == 'd':
            piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+1,topLefty+spaces))
            self.pieceMap[block.coordinate] = piece
        elif block.direction == 'r':
            piece = Rectangle(Point(topLeftx,topLefty), Point(topLeftx+spaces,topLefty+1))
        piece.setFill('red')
        piece.setOutline('white')
        piece.setWidth(2)
        piece.draw(self.win)

    def extract_coord(self, point):
        x = point.getX()
        y = point.getY()
        xindex = int(x)#rounds value
        yindex = int(y)
        return (xindex, yindex)

    def when_clicked(self, point):
        index = self.extract_coord(point)
        piece = self.coordMap[index]
        piece.setFill('red')
        if index in self.pieceMap:
            block = self.pieceMap[index]
            print block

    def test(self):
        car1 = car('A', (2,2), 'd')
        self.display_object(car1)

def mainloop():
    Canvas = Display()
    Canvas.test()
    while Canvas.win.isOpen():
        Point = Canvas.win.getMouse()
        Canvas.win.setMouseHandler(Canvas.when_clicked(Point))
        Canvas.win.flush()

if __name__ == "__main__":
    mainloop()

