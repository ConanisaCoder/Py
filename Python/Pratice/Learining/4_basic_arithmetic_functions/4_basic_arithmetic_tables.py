func = input("/ = Division, * = Mutilplication, + = Addtion, - = Subtraction: ")
if func == "/":
    num = float(input("What Number do you want to Divide: "))
    start = int(input("What number should the Table Start: "))
    stop = int(input("What number should the Table Stop at: "))
    for i in range(start,stop+1,1):
        total = num/i
        print(f"{num} / {i} = {total}")
        if total % 1 != 0:
            print(f"{num} / {i} = {round(total)}")
            print(f"{num} / {i} = {round(total,1)}")
        print("")
elif func == "*":
    num = float(input("What Number do you want to mutiply: "))
    start = int(input("Where do want the Table to start: "))
    stop = int(input("What number should the table end at: "))
    for i in range(start, stop + 1,1):
        total = num * i
        print(f"{num} * {i} = {total}")
        if total % 1 != 0:
            print(f"{num} * {i} = {round(total)}")
            print(f"{num} * {i} = {round(total,1)}")
        print("")
elif func == "+":
    num = float(input("What number do want yo add: "))
    start = int(input("Where should the table start: "))
    stop = int(input("Where should the table start: "))
    for i in range(start,stop+1,1):
        total =  num + i
        print(f"{num} + {i} = {total}")
        if total % 1 != 0:
            print(f"{num} + {i} = {round(total)}")
            print(f"{num} + {i} = {round(total,1)}")
        print("")
elif func == "-":
    num = float(input("The number you want to subtract: "))
    start = int(input("Where should the table start: "))
    stop = int(input("Where should the table start: "))
    for i in range(start,stop+1,1):
        total = num - i
        print(f"{num} + {i} = {total}")
        if total % 1 != 0:
            print(f"{num} + {i} = {round(total)}")
            print(f"{num} + {i} = {round(total,1)}")
        print("")
input("Enter to Close: ")