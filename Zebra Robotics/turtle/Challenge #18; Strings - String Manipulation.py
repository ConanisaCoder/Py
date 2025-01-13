'''
Create a program that takes 2 strings of length 10 and prints out:
The strings added together
The strings repeated 3 times
The strings converted to Uppercase AND added together
The strings converted to Lowercase AND repeated 5 times
The character at the 3rd index of each string
Both the strings sliced from index 3 to index 9
'''

string = input("First String: ")
string_2 =  input("Second String: ")
string_1 = string * 3
string_2_1 = string_2 * 3 
print(string_1)
print(string_2_1)
upper_string = string + string_2
upper_string = upper_string.upper()
print(upper_string)
lower_string = upper_string.lower() * 5
print(lower_string)
print(string[3])
print(string_2[3])
print(string[3:9])
print(string_2[3:9])