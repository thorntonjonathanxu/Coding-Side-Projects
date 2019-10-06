#The question we'll work through is the following: return a new sorted merged list from K sorted lists, each with size N. Before we move on any further, you should take some time to think about the solution!

def mergelist(x):
    foo = []
    for sub in x:
        for item in sub:
            foo.append(item)
    return sorted(foo)

x = [[10, 2],[5,3],[11,9]]
print(mergelist(x))