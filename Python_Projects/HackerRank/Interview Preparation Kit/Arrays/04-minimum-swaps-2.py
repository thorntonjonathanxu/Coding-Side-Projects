import math

def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        if(i+1 != arr[i]):
            count += 1
        print('i:{0} a[i]:{1} count = {2}'.format(i+1, arr[i],count))

    return math.ceil((count+1)/2)
# arr = [4,3,1,2]
# arr = [1,3,5,2,4,6,7]
# arr = [7,1,3,2,4,5,6]
print(minimumSwaps(arr))
