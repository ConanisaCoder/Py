import random
passwordchar = ""
z = 126-33+1
y = 33
for i in range(0,z,1):
    x = chr(y)
    passwordchar += x
    y += 1
password = ""
length = int(input("Enter the length of the password: "))
for i in range(0,length,1):
    x = random.randrange(0,len(passwordchar))
    index_pass = passwordchar[x]
    password += index_pass
print(password)
print("This is your genrated password:(" + password + ")" )