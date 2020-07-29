
#Must be a six digit number
#Value is within range of puzzle input
#Two adjacent digits are the same
#Digits only increase or stay the same


def validPassword(t):
    if(len(str(t)) != 6):
        return False
    AdjacentDigit = False
    lastDigit = 0

    list = [int(x) for x in str(t)]
    for char in list:
        if(char < lastDigit):
            return False
        if(char == lastDigit):
            AdjacentDigit = True
        lastDigit = char


min = 123257
max = 647015
i = min
count = 0
while (i != max):
    if(validPassword(i) == True):
        count = count + 1
    i = i+1
print(count)