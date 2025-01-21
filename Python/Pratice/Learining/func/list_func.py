print("Mistakes in this program may result in exit()")
x = input("Enter string: ")
y = input("Enter string: ")
z = input("Enter string: ")
list_func = [x , y , z]
run_program = input("Run program (y/n)?: ").lower()
while run_program == "y":
    print("(1) Add item(s) to list\n(2) Insert Item into list\n(3) Extend Items into list\n(4) Remove items from list\n(5) Clear\n(6) Index\n(7) Count\n(8) Sort\n(9) Reverse")
    choice =input("Enter Choice: ")
    if choice == "1":
        num = abs(int(input("Enter the amount of items you want to add: ")))
        for i in range(0,num,1):
            enter_item = input("Enter string: ")
            list.append(enter_item)
    elif choice == "2":
        num = abs(int(("Enter the Amount of strings to insert: ")))
        for i in range(0,num,1):
            index = input("Enter index starting at 0: ")
            if index > len(list_func) - 1:
                index = len(list_func) - 1
            else:
                index = index
            item = input("Enter Item: ")
            list.insert(index, item)
    elif choice == "3":
        x = input("Enter X: ")
        y  = input("Enter Y: ")
        list.extend([x,y])
    elif choice == "4":
        print(list_func)
        enter = input("Would you like to return the elements index(y/n)?: ")
        if enter == "n":
            num_remove = abs(int(input("Enter number of items to remove: ")))
            if num_remove > len(list_func) - 1:
                num_remove = len(list_func) - 1
            else:
                num_remove = num_remove
            for i in range(0,num_remove,1):
                print(list_func)
                remove = input("What would like to remove: ")
                if remove not in list_func:
                    print("Input Error")
                    print("Program will now end")
                    exit()
                list_func.remove(remove)
        elif remove == "y":
            num_remove = abs(int(input("Enter number of items to remove: ")))
            if num_remove > len(list_func) - 1:
                num_remove = len(list_func) - 1
            else:
                num_remove = num_remove
            for i in range(0,num_remove,1):
                pop = abs(int(input("Enter the index of the item you want to remove: ")))
                if pop > len(list_func) - 1:
                    pop = len(list_func) - 1
                else:
                    pop = pop
                list_func.pop(pop)
    elif choice == "5":
        list_func.clear()
        print("The list has been cleared")
    elif choice == "6":
        index = int(input("Enter index of item in list: "))
        if index > len(list_func) - 1:
            index = len(list_func)
        else:
            index = index
        print(list_func[index])
    elif choice == "7":
        count = abs(int(input("How many items do want count: ")))
        print(list_func)
        for i in range(0,count,1):
            count_item = input("What item should you wanna count: ") 
            print("There are"+ list_func.count(count_item) + (count_item))
    elif choice == "8":
        list_func.sort()
        print(list_func)
    elif choice == "9":
        list_func.reverse()
        print(list_func)