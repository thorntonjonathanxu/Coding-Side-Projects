from itertools import combinations

input_len = int(input())
input_str = input().split()
k = int(input())

# input_len = 4
# input_str = "aacd"
# k = 2


total = list(combinations(input_str,k))
subtotal = [i for i in total if 'a' in i]
print(len(subtotal)/len(total))