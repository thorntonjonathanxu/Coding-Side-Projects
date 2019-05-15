from itertools import combinations

# word = "HACK"
# num = 2
word,num = input().split()

for i in range(1,int(num)+1):
  comb = list(combinations(sorted(word),int(i)))
  for x in comb:
    print("".join(x))

