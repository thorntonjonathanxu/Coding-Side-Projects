import math
import random

#Need to do:
#1 Generate Random Start Point
#2 Calculate array based on a move

#Intailizes boardstate
board = [[0,0,0,0],[0,0,0,0],[0,2,0,0],[0,0,0,0]]

#Outputs intial board
[print(n, end=' \n') for n in board]

#Keyboard Inputs:
#0 - Left, 1 - Right, 2 - Up, 3 - Down
# if(input() == 0):
#     for row in board:
#         for i in row:
#             if(i == 0):