x = float(input("Enter Number Greater than one and Less than a Million: "))
while x < 1000000:
    print(x)
    if x % 2 ==  0: 
       x =  x * x 
    else:
        x = x * x * x