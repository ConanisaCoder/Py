print("Conversoin program of Byte to Decimal")
binary_num_test = input("Enter Byte number: ")
binary = ""
index = 0
total = 0
for i in range(0,len(binary_num_test),1):
    char = binary_num_test[index]
    binary += char
    index += 1
start = 2 ** (len(binary) - 1)
index = 0
for i in binary:
    char = binary[index]
    if index == 0:
        if char == "1":
            num_vaule =  start
        else:
             num_vaule = 0
    if index >= 1 :
            if char == "1":
                num_vaule =  start/2 ** index
            else:
                 num_vaule = 0
    total += num_vaule
    index += 1
print(total)