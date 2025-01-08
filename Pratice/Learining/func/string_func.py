run_program = input("run program (y/n): ").lower()
while run_program == "y":
    x = print("1.(Set String to lower Case)\n2.(Set String to Upper Case)\n3.(Len of String)\n4.(Remove whitespace removed from start and end) \n5.(isalpha) \n6.(is.digit)\n7.(startswith)\n8.(endswith)\n9.(find)\n10.(replace)")
    string = input("Enter string: ")
    if x == "1":
        print(string.lower())
    elif x == "2":
        print(string.upper())
    elif x == "3":
        print(len(string))
    elif x == "4":
        print(string.strip())
    elif x == "5":
        print(string.isalpha())
    elif x == "6":
        print(string.isdigit())
    elif x == "7":
        start = input("does it start with?: ")
        print(string.startswith(start))
    elif x == "8":
        end = input("does it end with?: ")
        print(string.endswith(end))
    elif x == "9":
        find = input("What do you want to find?: ")
        print(string.find(find))
    elif x == "10":
        replace_t_f = input("replace whole string (y/n): ").lower()
        if replace_t_f == "y":
            enter_replace = input("Enter replacement: ")
            string.replace(enter_replace)
        elif replace_t_f == "f":
            what_replace = input("What to replace in this string: ")
            enter_replace = input("Enter replacement: ")
            string.replace(what_replace, enter_replace)
