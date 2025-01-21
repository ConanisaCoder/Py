'''
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
'''
string = input("Enter string: ").strip()
rev_string = ""
index = -1
for i in string:
    char = string[index]
    index += -1
    rev_string += char
if rev_string == string:
    print("This a palindrome ")
else: 
    print("This not a palindrome")