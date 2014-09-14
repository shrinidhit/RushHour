"""
2048 Text Rendition: Not pretty, but has basic functionality
Created by Shrinidhi Thirumalai
9/7/14
"""
from random import choice
from random import randint
from math import log
score = 0

# Creates starting Grid, which each location as a tuple
def create_grid():
	Grid = {}
	# Loops through all rows and columns, fills with None
	for row in range(1, 5):
		for column in range(1,5):
			Grid[(row,column)] = None
	# Inserts 2 or 4 randomly into two random places on the grid
	for starting_nums in range(0,2):
		filled_row = randint(1,4)
		filled_column = randint(1,4)
		Grid[(filled_row, filled_column)] = choice([2,4])
	return Grid

#Prints Grid as array output
def print_grid(Grid):
	# Loops through all rows and columns, prints
	for row in range(1, 5):
		for column in range(1,5):
			if Grid[(row,column)] == None:
				print "_  ",
			else:
				print str(Grid[(row,column)]) + '  ',
		print("\n")
	print('\n')

#Defines next tile for each direction
def step((row, column), direction):
	if direction == 'up' and row <4:
		return (row + 1, column)
	elif direction == 'down' and row >1:
		return (row - 1, column)
	elif direction == 'right' and column >1:
		return (row, column - 1)
	elif direction == 'left' and column <4:
		return (row, column + 1)
	else: 
		return 'NoTile'

#Defines Past tile for each direction
def past((row, column), direction):
	if direction == 'up' and row >1:
		return (row - 1, column)
	elif direction == 'down' and row <4:
		return (row + 1, column)
	elif direction == 'right' and column <4:
		return (row, column + 1)
	elif direction == 'left' and column >1:
		return (row, column - 1)
	else: 
		return 'NoTile'

#Pushes one line to a direction given(location is the "line" that is pushed, either a column or row)
def pushline(Grid, location, direction):
	#Gets order of for loop depending on direction of push
	if direction == "up" or direction == "left":
		shiftdirection = 1
		Order = range(1, 5, shiftdirection)
	elif direction == "down" or direction == "right":
		shiftdirection = -1
		Order = range(4, 0, shiftdirection)
	#Combines tiles next to eachother of same number
	for i in Order:
		if direction == "up" or direction == "down":
			current_tile = (i, location)
		elif direction == "right" or direction == "left":
			current_tile = (location, i)
		next_tile = step(current_tile, direction)
		past_tile = past(current_tile, direction)
		if past_tile != 'NoTile' and Grid[past_tile] != None and Grid[past_tile] == Grid[current_tile]:
			Grid[past_tile] = Grid[past_tile] + Grid[current_tile]
			global score
			score = score + return_score_increase(Grid[past_tile])
			Grid[current_tile] = None
			i = i - shiftdirection
	#Pushes tiles to a side
	for i in Order:
		if direction == "up" or direction == "down":
			current_tile = (i, location)
		elif direction == "right" or direction == "left":
			current_tile = (location, i)
		next_tile = step(current_tile, direction)
		past_tile = past(current_tile, direction)
		while next_tile != 'NoTile' and Grid[current_tile] == None:
			Grid[current_tile] = Grid[next_tile]
			Grid[next_tile] = None
			next_tile = step(next_tile, direction)

		
	return Grid

#Pushes all lines in grid to a given direction, and places a new random tile
def push(Grid, direction):
	#Pushes all lines
	for i in range(1,5):
		pushline(Grid, i, direction)
	#Replaces a random empty tile
	replace = True
	while replace:
		location = (randint(1,4), randint(1,4))
		if Grid[location] == None:
			Grid[location] = choice([2,4])
			replace = False
	return Grid
 
#Checks if grid is full to end game
def check_full(Grid):
    for row in range(1,5):
        for column in range(1,5):
            if Grid[(row, column)] == None:
                return True
    return False

#Checks if 2048 has been reached
def check_2048(Grid):
    for row in range(1,5):
        for column in range(1,5):
            if Grid[(row, column)] == 2048:
                return False
    return True

#Returns Score increase
def return_score_increase(value):
	return value * (log(value, 2) - 1)
	
#Game Sequence
def Game():
    running = True
    Grid = create_grid()
    print_grid(Grid)
    while running:
        arrow = raw_input("Enter direction(""up"", ""down"", ""right"", ""left""): ")
        Grid = push(Grid, arrow)
        print "Score = " + str(score)
        print_grid(Grid)
        running = check_full(Grid)
        running = check_2048(Grid)
    print "Game Over"

#Main Script:
if __name__ == '__main__':
	Game()