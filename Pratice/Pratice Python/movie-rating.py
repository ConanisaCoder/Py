age = input("What is your age: ")
age = int(age)
if age > 17:
    print("You can see an R movie")
elif age < 17 and age> 12:
    print("can see a rated PG-13 movie")
else:
    print("You can only see PG")