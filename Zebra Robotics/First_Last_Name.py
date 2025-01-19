def formant_name(name):
    name_List = name.split("-")
    return name_List[0] , name_List[len(name_List) - 1]
name_count = int(input("Enter number of Names: "))
for i in range(0,name_count,1):
    name = input("Enter name with 'put -': ")
    first_name, second_name = formant_name(name)
    print(first_name , second_name)
