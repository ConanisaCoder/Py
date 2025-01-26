import random
def password_Generator(length,norm_char=True): 
     password =""
     char = "QWERTYUIOPLASDFGHJKLZXCVNBM1234567890qwertyuioplkjhgfdsazxcvbnm"
     speical_char = r"QWERTYUIOPLASDFGHJKLZXCVNBM1234567890qwertyuioplkjhgfdsazxcvbnm!@#$%^&*()`~-_+=[]{}'/?.>,<;:\|"       
     for i in range(length): 
        if norm_char:
            password += char[random.randrange(0,len(char) - 1)]
        else:
            password += speical_char[random.randrange(0,len(speical_char) - 1)]
     return password    

while True:
    try:
        length = int(input("How long do you want the password to be: "))
        break
    except ValueError:
        print("Enter int Vaule")
speical_char = input("Speical char (y/n): ").lower()
if speical_char == "n":
    print(password_Generator(length,True))
elif speical_char == "y":
    print(password_Generator(length,False))
