from itertools import combinations_with_replacement

word = "HACK"
num = 2
# word,num = input().split()

comb = list(combinations_with_replacement(sorted(word),int(num)))
for x in comb:
  print("".join(x))

