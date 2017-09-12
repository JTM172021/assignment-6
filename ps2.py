###### this is the ps2 .py file ###########

#function to print tic tac toe board

def print_board():
	for i in range(0,3):
		for j in range(0,3):
			print map[2-i][j]
			if j!=2:
				print "|"
		print ""

def playgame():

print "Welcome to the game"

print "player 1 chance(choose numbers 1,3,5,7,9)"
print "Enter the position and number to be entered:"
pos=int(raw_input())
num=int(raw_input())
grid=[]
gridresetgrid(grid)
