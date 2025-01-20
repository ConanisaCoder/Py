'''
Simple Encryption Program allows the user to 
move charcters 
and convert encrpted vaules 
'''
action = input("What would you like to do Encryption or Decryption(E/D): ")
if action.lower() == "e":
    sentence = input("Enter sentence: ")
    index = 0
    encrpytion_mesg = ""
    for i in sentence:
        char = sentence[index]
        char = chr(ord(char) + 1)
        encrpytion_mesg += char
        index += 1
    print(encrpytion_mesg)
if action.lower() == "d": 
    message = input("Enter Message: ")
    moves = int(input("How many places was this value moved: "))
    index = 0
    decryption_mesg = ""
    for i in message:
        char = message[index]
        char = chr(ord(char) - moves)
        decryption_mesg += char
        index += 1
    print(decryption_mesg)