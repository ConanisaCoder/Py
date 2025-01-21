print("(1) Add mutiple strings strings\n(2) Index a string\n(3) Mutiply a String\n(4) Enter a quote")
item = input("What you like to do this string: ")
string = ""
if item == "1":
    count = int(input("How many Strings: "))
    for i in range (0,count,1):
        new_var = input("Input: ")
        string += new_var
    print(string)
if item == "2":
    string = input("Enter string: ")
    print(string)
    x =int(input("Enter Index (Starts from zero): "))
    print(string[x])
if item == "3": 
    string = input("Enter String: ") * 3
    print(string)
if item == "4":
    person = input("Enter the Person who said this: " )
    quote = input("Enter quote: ")
    print(f"\"{quote}\"-{person}")