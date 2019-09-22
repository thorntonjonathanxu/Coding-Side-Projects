def staircount(n,X):
    #Fibonacci Sequence with generic 1 and 2 steps.
    # if(n <= 1):
    #     return 1
    # return staircount(n-1) + staircount(n-2)

    #Basic Fibonacci calculator 
    # a,b = 1, 2
    # for _ in range(n-1):
    #    a,b = b, a + b
    # return a 

    #Order O(X^n)
    # if(n < 0):
    #     return 0
    # elif(n==0):
    #     return 1
    # else:
    #     return sum(staircount(n-x,X) for x in X)

    cache = [0 for _ in range(n+1)]
    cache[0] = 1
    for i in range(1, n+1):
        cache[i] = sum(cache[i-x] for x in X if i - x >=0)
    return cache[n]


print(staircount(5,[1,3,5]))