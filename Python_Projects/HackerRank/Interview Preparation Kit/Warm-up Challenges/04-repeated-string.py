
def repeatedString(s, n):
	# 1. s.count('a') counts the total number of 'a' in a full substring
	# 2. (n//len(s)) calculates the total number of full substrings based on the provided N size. Need to take floor so the remainder can be calcuated.
	# 3. Multily the count of 'a' by the total number of full substrings.
	# 4. Add the total number of 'a' in the incomplete substring and return this value.
	return (s.count('a') * (n//len(s)) + s[:n % len(s)].count('a'))

#Test Case
# s = 'aba'
# n = 10
s = input()
n = int(input())
print(repeatedString(s,n))
