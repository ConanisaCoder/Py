operator = input("Enter the Operator (+, -, *, /): ")

if operator == "+":
    n_1 = float(input("Number One: "))
    n_2 = float(input("Number Two: "))
    total = n_1 + n_2
    total_round = round(total)
    yn = input("Would you Like the Total Rounded (Y/N): ")
    if yn == ("Y" or "Yes"):
        print(f"The total of these two numbers is {total}")
        print(f"The total of these two numbers rounded is {total_round}")
        input("Press enter to close: ")
    elif yn == ("N" or "no"):
        print(f"The sum of these two numbers is {total}")
        input("Press enter to close: ")
elif operator == "-":
    n_1 = float(input("Number One: "))
    n_2 = float(input("Number Two: "))
    total = n_1 - n_2
    total_round = round(total)
    yn = input("Would you Like the Diffrence Rounded (Y/N): ")
    if yn == ("Y" or "Yes") :
        print(f"The diffrence of these two numbers is {total}")
        print(f"The diffrence of these two numbers rounded is {total_round}")
        input("Press enter to close: ")
    if yn == ("N" or "No"):
        print(f"The diffrence of these two numbers {total}")
        input("Press Enter to Close: ")
elif operator == "*":
    n_1 = float(input("Number One: "))
    n_2 = float(input("Number Two: "))
    total = n_1 * n_2
    total_round = round(total)
    yn = input("Would you Like the Product Rounded (Y/N): ")
    if yn == ("Y" or "Yes"):
        print(f"The product of these two numbers is {total}")
        print(f"The prodcut of these two number rounded is {total_round}")
        input("Press Enter to Close: ")
    if yn == ("No" or "N"):
        print(f"The product of these two numbers is {total}")
        input("Press Enter to Close: ")
elif operator == "/":
    n_1 = float(input("Number One: "))
    n_2 = float(input("Number Two: "))
    total = n_1 / n_2
    total_round2 = round(total)
    total_reminder = n_1 % n_2
    yn = input ("Would you Like to round and and get the reminder (Y/N): ")    
    if total_reminder >= 1: 
        print(f"The quotient of these two numbers is {total}")
        print(f"The quotient rounded is {total_round2}")
        print(f"The reminder is {total_reminder}")
        input("Press Enter to Close: ")
    elif total_reminder == (0.0 or 0):
        print(f"The quotient of these two numbers is {total}")
        input("Press Enter to Close: ")