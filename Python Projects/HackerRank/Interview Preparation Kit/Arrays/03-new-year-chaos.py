#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.

#1. Parse through the list to see if element in a given index is greater than the active index. Since an element can only swap at most twice, if the array location is greater than 2 hoops we return 'Too chaotic'
#2. To cont...
def minimumBribes(q):
    count = 0
    for i in range(len(q)):
        print()
        print('{0} - {1} = {2}'.format(q[i], (i+1), (q[i] - (i + 1))))

        if(q[i] - (i + 1) > 2):
            return 'Too chaotic'
        for j in range(max(0,q[i] - 2),i):
            print('{0} > {1}'.format(q[j], q[i]))
            print(count)

            if(q[j] > q[i]):
                count += 1
    return count

#Test Cases
# q = [2,1,5,3,4]
# q = [2,5,1,3,4]
# q = [5,1,2,3,7,8,6,4]
q = [1,2,5,3,7,8,6,4]


print(minimumBribes(q))

# if __name__ == '__main__':
#     t = int(input())

#     for t_itr in range(t):
#         n = int(input())

#         q = list(map(int, input().rstrip().split()))

#         minimumBribes(q)
