'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
num = int(input("Enter number: "))
test_divisor = 1
list_divisor = []
while num >= test_divisor:
    if num % test_divisor == 0:
        list_divisor.append(test_divisor)
        test_divisor +=1 
    else:
        test_divisor +=1 
print(list_divisor)