from itertools import permutations

# word = "HACK"
# num = 2
word,num = input().split()

perm = list(permutations(word,int(num)))
perm.sort()
for x in perm:
  print("".join(x))

