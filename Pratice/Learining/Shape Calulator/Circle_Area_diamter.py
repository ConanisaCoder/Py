import math
diameter = input("What is the dimeter of a cirlce: ")
diameter = (float(diameter))


Area = (math.pi *pow(diameter,2))/4
Area_rounded = round(Area)

print(f"The Area of this Cirlce is {Area} units² ")
print(f"The Area of this Cirlce rounded is {Area_rounded} units² ")
Done = input("Press Enter When You Are Done: ")