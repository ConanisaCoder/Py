def stringToList(string,vaule=False):
    list_string = []
    for i in string:
        list_string.append(i)
    if vaule == True:
        list_string = list_string[::-1]
        print(list_string)
        return list_string
    else: 
        print(list_string)
        return list_string
string = input("Enter string: ")
vaule = input("Enter vaule(t/f): ").lower()
if vaule == "t":
    stringToList(string,True)
elif vaule == "f":
    stringToList(string,False)
