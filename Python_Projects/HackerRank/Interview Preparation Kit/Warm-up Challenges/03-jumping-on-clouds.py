#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):

    count = 0
    i = 0 
    while (i < n-1):
        i += (c[i+2] == 0) + 1
        count += 1  
    return count
      
n = int(input())
c = list(map(int,input().strip().split()))
c.insert(n,0)
print(jumpingOnClouds(n,c))

