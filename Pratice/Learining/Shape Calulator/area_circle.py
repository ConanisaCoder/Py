import math
W = input ("D = Diameter, R = Raduis, C = Circumfrence :")
if W == "D":
    diameter = input("What is the dimeter of a cirlce: ")
    diameter = (float(diameter))
    Area = (math.pi *pow(diameter,2))/4
    Area_rounded = round(Area)
    print(f"The Area of this Cirlce is {Area} units² ")
    print(f"The Area of this Cirlce rounded is {Area_rounded} units² ")
    Done = input("Press Enter When You Are Done: ")
elif W == "R":
    raduis = float(input("What is the Raduis of the Cirlce: "))
    Area = math.pi * pow(raduis, 2)
    Area_rounded = round(Area)
    print(f"The Area of this Circle is {Area} units²    ")
    print(f"The Rounded Area of this Circle is {Area_rounded} units²    ")
    Done = input("Press Enter When You Are Done: ")
elif W == "C":
    circumference = input("What is the circumference of the Circle: ")
    circumference = float(circumference)
    radius = (circumference/( 2* math.pi ))
    Area = math.pi * pow(radius, 2)
    Area_rounded = round(Area)
    print(f"The Area of this Circle is {Area} units²    ")
    print(f"The Rounded Area of this Circle is {Area_rounded} units²    ")
    Done = input("Press Enter When You Are Done: ")


