print("(1) Add\n(2) Subtract\n(3) Divide\n(4) Mutiplication\(5) Power\n(6) Floor division\n(7) Modulus")
z = input("Enter numbers: ")
if z == "4":
    x = float(input("Enter factor: "))
    y = float(input("Enter factor: "))
    print(x*y)
if z == "1":
    x = float(input("Enter Addend: "))
    y = float(input("Enter Addend: "))
    print(x + y)
if z == "2":
    x = float(input("Enter Minued: "))
    y = float(input("Enter Subtrahend: "))
    print(x-y)
if z == "3":
    x = float(input("Enter dividend: "))
    y = float(input("Enter Divisor: "))
    print(x/y)
if z == "5":
    x = float(input("Enter base: "))
    y = float(input("Enter exponent: "))
if z == 6: 
    x = float(input("Enter dividend: "))
    y = float(input("Enter divsior: "))
    print(x//y)
if z == 7: 
    x = float(input("Enter dividend "))
    y = float(input("Enter Divisor: "))
    print(x%y)