list_input = []
num_input = abs(int(input("Enter the amount of numbers: ")))
new_list = []
for i in range (0,num_input,1):
    num_add = (int(input("Enter the number: ")))
    list_input.append(num_add)
index = 0
for i in list_input:
    char = list_input[index]
    if char < 5:
        new_list.append(char)
        index+= 1
    else:
      index+= 1  
print(new_list)
    
