
a = int(input("Enter Number Greater than 1 and less than 50,000: "))#

while a != 1 and a <= 50000:
    print(a)
    if a % 2 == 0:  # If `a` is even
        a //= 2
    else:           # If `a` is odd
        a = (a * 3) + 1