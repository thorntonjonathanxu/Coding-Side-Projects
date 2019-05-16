
import math
import os
import random
import re
import sys

#Runtime O(n*m)

#1. Build out the hourglass values in a double nested for loop. Since it's loop two rows and two columns ahead it would be 6-2 = 4 for the range
#2. Appened the total sum for each hourglass into a list.
#3. Return the max value in the sum list

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourSums = []
    for i in range(4):          #These are the column
        for j in range (4):     #These are the rows
            hourSums.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

            # Test print cases
            # print(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            # print('{0} {1} {2}'.format(arr[i][j], arr[i][j+1], arr[i][j+2]))
            # print('  {0}  '.format(arr[i+1][j+1],))
            # print('{0} {1} {2}\n'.format(arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]))
    return(max(hourSums))

            
#Test Case
# arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

# Array indices testing
# arr = [[1,2,3,4,5,6],
# [7,8,9,10,11,12],
# [13,14,15,16,17,18],
# [19,20,21,22,23,24],
# [25,26,27,28,29,30],
# [31,32,33,34,35,36]]

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
print(hourglassSum(arr))
