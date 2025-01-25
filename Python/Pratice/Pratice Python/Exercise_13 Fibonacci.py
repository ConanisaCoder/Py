a,b = 1,0
user_input =int(input("Enter bumber to genrate: "))
for i in range(user_input):
    a,b = b , a+b
    print(a)
