#!/bin/python3

import math
import os
import random
import re
import sys

#Objective is to rearrange an array based on a provided n indicies. We can use the array index to slipt based on provided value.
#Return the upper part of the list first then the lower part of the list second.

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]

#Test Case
d = 4
a = [1,2,3,4,5]

print(rotLeft(a,d))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nd = input().split()

#     n = int(nd[0])

#     d = int(nd[1])

#     a = list(map(int, input().rstrip().split()))

#     result = rotLeft(a, d)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
