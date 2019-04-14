# # #Hacker Rank sWAP cASE
# # input = 'Www.HackerRank.com → wWW.hACKERrANK.COM'
# # print(input + '\n' + input.swapcase())


# # #String Split and Join
# # input = 'this is a string'
# # print(input.replace(' ', '-'))

# # #Input with Strings
# # a = 'foo'
# # b = 'Peet'
# # def print_full_name(a, b):
# #     return('Hello {0} {1}! You just delved into python.'.format(a,b))

# # print_full_name(a,b)

# # #Mutations
# # s = 'abracadabra'
# # position = 5
# # character = 'k'

# # print(s[0:position] + character + s[(position+1):])

# # #Find a String
# # string = 'ABCDCDC'
# # sub_string = 'CDC'

# # total = 0
# # i = 0
# # while(i <= len(string)-len(sub_string)):
# #     if(string[i:i+len(sub_string)]== sub_string):
# #         print('{0}  -  {1}'.format(string[i:i+len(sub_string)],sub_string))
# #         total += 1
# #     i += 1
# # print(total)

# #String Validation

# s = 'qA2'
# print (any(c.isalnum() for c in s))
# print (any(c.isalpha() for c in s))
# print (any(c.isdigit() for c in s))
# print (any(c.islower() for c in s))
# print (any(c.isupper() for c in s))

# #Text Wrap
# string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# max_width = 4

# def wrap (string, max_width):
#     output = ''
#     while(max_width <= len(string)):
#         output += '{0}\n'.format(string[0:max_width])
#         string = string[max_width:]
#     output += string
#     return output

# print(wrap(string,max_width))

# import math
# #Designer Door
# n,m  = [int(x) for x in input().split()]   
# i = 1
# output = ''
# while(i<= ((m-1)/3)):
#     output +='{0}{1}{2}\n'.format('-'*int(math.floor((m-i*3)/2)),'.|.'*i,'-'*int(math.floor((m-i*3)/2)))
#     i += 2
# output += '{0}WELCOME{1}\n'.format('-'*int((m-7)/2),'-'*int((m-7)/2))
# i -= 2
# while(i>= 1):
#     output +='{0}{1}{2}\n'.format('-'*int(math.floor((m-i*3)/2)),'.|.'*i,'-'*int(math.floor((m-i*3)/2)))
#     i -= 2
# print(output)

# #String Formatting
# def print_formatted(number):
#     [print('{0} {1} {2} {3}'.format(i,oct(i),str(hex(i)).upper(),bin(i))) for i in range(1, number)]

# foo = 17
# print_formatted(foo)
# def wrap(string, max_width):
#     return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])


input = 'BANANA'
letters = list(input)
vowel = []
consonant = [] 
for n in letters:
    if n in {'A','E','I','O','U'}:
        vowel.append(n)
    else:
        consonant.append(n)

# print(sum('A' in s for s in input))
print(consonant)

def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in xrange(length):
    for j in xrange(i,length):
      alist.append(string[i:j + 1]) 
  return alist

print get_all_substring('abcde')
