
# 1. Purpose of this solution is to count each instance of when our 'location' returns to 0 from a negative number.
# 2. When location goes from -1 to 0, we increment 'valley' variable by 1.
# 3. Any step up is +1, any step down is -1.

def countingValleys(n, s):
    location = valley = 0
    for step in s:
        if(step == 'U'):
            if(location == -1):
                valley += 1
            location += 1
        else:
            location += -1
    return valley

#Test Cases
# n = 8
# s = 'UDDDUDUU'

n = int(input())
s = input()
print(countingValleys(n,s))