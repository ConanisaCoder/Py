def bytes_to_text():
    bytes_num = abs(int(input("How many bytes are here: ")))
    string = ""
    val = 0
    bytes_to_text=""
    for i in range(0,bytes_num,1):
        binary_val = input("Enter binary value: ")
        index = 0
        binary_false_string = ""
        for i in binary_val:
            char = binary_val[index]
            if char in "01":
                binary_val += binary_false_string
                index += 1
            else:
                index+=1
        index = 0
        for i in binary_false_string:
            val = 0
            char = binary_false_string[index]
            if char == "1":
                if index == 0:
                    val += ((len(binary_false_string))**2) /2 
                    bytes_to_text += chr(val)
                if index >= 1:
                    val += ((len(binary_false_string))**2) / index * 2
                    bytes_to_text += chr(val)
            elif char == "0":
                val += 0
                bytes_to_text += chr(val)
            index +=1
    print(bytes_to_text)
bytes_to_text()