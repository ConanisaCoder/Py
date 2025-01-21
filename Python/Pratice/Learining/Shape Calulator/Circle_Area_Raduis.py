import math
raduis = float(input("What is the Raduis of the Cirlce: "))


Area = math.pi * pow(raduis, 2)
Area_rounded = round(Area)

print(f"The Area of this Circle is {Area} units²    ")
print(f"The Rounded Area of this Circle is {Area_rounded} units²    ")

Done = input("Press Enter When You Are Done: ")

