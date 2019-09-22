

# witnesses = [5,3,0,2,6,2,0,7,2,5]

def stripZeros(input):
    #Remove 0's from list
    foo = []
    for n in input:
        if(n != 0):
            foo.append(n)
    return foo    

# def descSort(input):
#     # Returns the list stored in decending order    
#     input.sort(reverse=True)
#     return input

def sizeCheck(n,input):
    # Returns if n is larger than provided list 
    if(len(input) == 0 and n > 0):
        return True  
    return (n > len(input))

def subListSubtraction(n, input):
    # Subtracts 1 from each element in sublis
    foo = []
    for elem in range(n):
        foo.append(input[elem] - 1)
    foo = foo + input[n:]
    return foo

# list = [5,3,0,2,6,2,0,7,2,5]
# print(stripZeros(list))
# print(descSort(list))

# #Warmup 3 Test Cases
# print(sizeCheck(7, [6, 5, 5, 3, 2, 2, 2])) 
# print(sizeCheck(5, [5, 5, 5, 5, 5])) 
# print(sizeCheck(5, [5, 5, 5, 5])) 
# print(sizeCheck(3, [1, 1])) 
# print(sizeCheck(1, []))
# print(sizeCheck(0, []))

# #Warmup 4 Test Cases
# print(subListSubtraction(4, [5, 4, 3, 2, 1]))
# print(subListSubtraction(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]))
# print(subListSubtraction(1, [10, 10, 10]))
# print(subListSubtraction(3, [10, 10, 10]))
# print(subListSubtraction(1, [1]))

def hh(list):
    # Remove all 0's from the sequence (i.e. warmup1).
    temp = stripZeros(list)
    # If the sequence is now empty (no elements left), stop and return true.
    if(len(temp) == 0):
        return True
    # Sort the sequence in descending order (i.e. warmup2).
    temp = temp.sort(reverse=True)
    # Remove the first answer (which is also the largest answer, or tied for the largest) from the sequence and call it N. The sequence is now 1 shorter than it was after the previous step.
    n = temp[0]
    temp = temp [1:]
    # If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
    if(sizeCheck(n,temp)):
        return False
    # Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).
    temp = subListSubtraction(n,temp)
    # Continue from step 1 using the sequence from the previous step.

    

#Havel Hakimi Test Cases
print(hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]))
# print(hh([4, 2, 0, 1, 5, 0]))
# print(hh([3, 1, 2, 3, 1, 0]))
# print(hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
# print(hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]))
# print(hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))
# print(hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))
# print(hh([2, 2, 0]))
# print(hh([3, 2, 1]))
# print(hh([1, 1]))
# print(hh([1]))
# print(hh([]))