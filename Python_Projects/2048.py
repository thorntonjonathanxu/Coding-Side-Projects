import math
import random

#Need to do:
#1 Generate Random Start Point
#2 Calculate array based on a move

#Intailizes boardstate
board = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0],  
[0,0,0,0]]

def moveUp():
    for i in board:
        i = slide(i)
        print('{0}\n'.format(i))
    return board

def addTile():
    options = []
    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0):
                options.append([i,j])
    if(len(options) > 0):
        update = random.choice(options)
        board[update[0]][update[1]] = random.choice([2,4])
    return board
    # return options

def displayBoard():
    print()
    [print(n, end=' \n') for n in board]

def slide(row):
    arr = [i for i in row if i > 0]
    [arr.append(0) for i in range(4 - len(arr))]
    return arr
#Outputs intial board
displayBoard()
addTile()
addTile()
displayBoard()
moveUp()
addTile()
displayBoard()

#Look for the first empty register/Save that to a local variable
#Look through column/row for next instance of value 

#Keyboard Inputs:
# 0 - Left, 1 - Right, 2 - Up, 3 - Down
# if(input() == 0):
#     for row in board:
#         for i in row:
#             if(i == 0):
                