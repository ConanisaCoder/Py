import math

find = input("Do you have the Length Hypotenuse (Y/N): ")
if find == "Y":
    a = float(input("Enter the length of side A: "))
    b = float(input("Enter the length of side B: "))
    h = (a ** 2 + b ** 2) ** 0.5
    p = h + a + b

    Side_C = math.sqrt(pow(a, 2) + pow(b, 2))
    Side_C_Round = math.round(Side_C)


    print(f"The length of Side C is {h} Units")
    print(f"The length of Side C is {h} Units")
    done = input("Press Enter to Close: ")

elif find == "N":
    a = float(input("Enter the length of side A: "))
    e = float(input("Enter the Length of E: "))
    c = math.sqrt(e ** 2 - a ** 2)
    print(f"The length of the missing Side is {c} Units")
    done = input("Press Enter to Close: ")