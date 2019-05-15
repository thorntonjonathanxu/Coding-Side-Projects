from itertools import product

m = list(map(int, input().split()))
n = list(map(int, input().split()))
print(*product(m,n))
