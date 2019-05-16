from collections import Counter

#Counter aggregates items in to specific list. 
#	Counter(ar).keys() generates a list of unique keys in the provided list
#	Counter(ar).values() generates a count of each unquie key in the provided list

# 1. Aggregate list in to a counter with the total number of sets
# 2. Count each pair of 2 in the list for any values greater than 2. 
# 3. If the subset has an odd number it will take the floor of the value
# 4. Returns total number of pairs

def sockMerchant(n, ar):
	count = 0
	for val in Counter(ar).values():
		if(val % 2 == 0) or (val >=2):
			count += val//2
	return count

#Test Case
# n = 9
# ar = [10,20,20,10,10,30,50,10,20]

#
n = input()
ar = input().strip()
print(sockMerchant(n,ar))	