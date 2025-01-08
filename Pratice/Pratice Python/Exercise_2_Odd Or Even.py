x =  input("Start (Y/N): ")

while x == "Y": 
    print("Even or odd")
    num = input("Enter Number: ")
    num = int(num)
    num_e_o_odd = num % 2 
    print("This number is even" if num_e_o_odd == 0 else " This number is odd")
    x =  input("Go again (Y/N): ")
else:
    input("Enter to close: ")