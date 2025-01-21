'''
Program for Trignormty ratios
'''
import math
x = input("Run program ('Y'/ 'Yes': ")
while x == "Y" or "Yes": 
    find = input("What are you trig ratio will you be using ('TAN' or T)/('SIN' or 'S')/(COS/'C'): ")
    if find == "Tan" or "TAN" or "T":
        Tan_find = input("What are you solving for ('Angle'/'Side'): ")
        if Tan_find == "Angle":
            oppsite = float(input("What is length of the oppsite side: "))
            adjacent = float(input("What is the adjacent: "))
            tan_ratio = oppsite/adjacent
            tan_angle = math.degrees(math.atan(tan_ratio))
            print(f"The tangnet ratio is {tan_ratio} and angle is {tan_angle} degreees.", end="")
            print(f"Rounded angle is {round(tan_angle)} degrees.")
        elif Tan_find == "Side":
            Tan_find = input("What are finding Oppsite or Adjcent ('OPP'/'ADJ'): ")
            if Tan_find == "OPP" :
                Tan_Angle = (float(input("What is the angle: ")))
                adjacent = input("What is the adjacent: ")
                Tan_Angle_1 = math.tan(math.radians(Tan_Angle))
                adjacent = float(adjacent)
                oppsite = Tan_Angle_1 * adjacent 
                print(f"The length of the side you are looking for (The oppsite side of the Angle) {oppsite} units and {round(oppsite)} units.") 
            elif Tan_find == "ADJ":
                oppsite = float(input("What is the length of the oppsite angle: "))
                Tan_Angle = float(input("What is the angle: "))
                Tan_Angle = math.tan(math.radians(Tan_Angle))
                adjacent = oppsite / Tan_Angle
                print(f" The length of the missing side is {adjacent} units and {round(adjacent)} units.")
    if find == "Sin" or "SIN" or "S":
        Sin_Find_Side_S= input("What are you solving for ('Angle'/'Side'): ")
        if Sin_Find_Side_S ==  "Angle":
            oppsite =float(input("What is the Length of the Oppsite: "))
            Hyptonuse = float(input("What is the Length of the Hyptonuse: "))
            Sin_Ratio = oppsite/Hyptonuse
            Angle = math.degrees(math.atan(Sin_Ratio))
            print(f"The Angle in degress is {Angle}, {round(Angle)} when rounded and the Sin ratio is {Sin_Ratio}")
        elif Sin_Find_Side_S== "Side":
            Sin_Find_Side_S = input("What are you trying to find ('OPP'/'HYP'): ")
            if Sin_Find_Side_S == "OPP":
                Sin_Angle = float(input("What the Angle given: "))
                Hyptonuse = float(input("What is the Length of Hyptonuse: "))
                oppsite = math.sin(math.radians(Sin_Angle)) * Hyptonuse
                print(f"The length of the oppsite angle is {oppsite} units and {round(oppsite)} units.")
            if Sin_Find_Side_S == "HYP":
                Angle = float(input("Input the Angle: "))
                oppsite = float(input("Input the oppsite side: "))
                Sin_Find = math.sin(math.radians(Angle))
                Hyptonuse = oppsite /Sin_Find
                print(f"The length of the Hyptonuse is {Hyptonuse} units, when rounded it is {round(Hyptonuse)}.")
    if find == "COS" or "Cos" or "C":
        Cos_Find = input("What are you trying to find ('Angle/Side'): ")
        if Cos_Find == "Side":
            Side_Find_Side_C = input("What side are your trying to find ('ADJ'/'HYP'): ")
            if Side_Find_Side_C == "ADJ": 
                Angle = float(input("What is the angle in degrees: "))
                Hyptonuse = float(input("What is the length of the hyptonuse: "))
                Angle_cov = math.cos(math.radians(Angle))
                adjacent = Angle_cov * Hyptonuse
                print(f"The length of the adjacent is {adjacent}, when round is {round(adjacent)}")
            if Side_Find_Side_C == "HPY":
                adjacent = float(input("What is the adjacent of the traingle: "))
                Angle =  float(input("What is the angle in degrees of this traingle"))
                Angle_conv = math.cos(math.radains(Angle))
                Hyptonuse = adjacent / Angle_conv
                print(f"The length of hyptonuse is {Hyptonuse}, when rounded is {round(Hyptonuse)}")
        elif Cos_Find == "Angle":  
            adjacent = float(input("What is the adjacent: "))
            Hyptonuse =  float(input("What is the Hypotonuse: "))
            Angle = math.degrees(math.acos(adjacent/Hyptonuse))
            print(f"The Angle is {Angle} degress , when rounded is {round(Angle)} degrees")
    x = input("Go again (Y/N): ")
else:
    input("Enter to close: ")