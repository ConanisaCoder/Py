import math

circumference = input("What is the circumference of the Circle: ")
circumference = float(circumference)

radius = (circumference/( 2* math.pi ))

Area = math.pi * pow(radius, 2)
Area_rounded = round(Area)

print(f"The Area of this Circle is {Area} units²    ")
print(f"The Rounded Area of this Circle is {Area_rounded} units²    ")

Done = input("Press Enter When You Are Done: ")
