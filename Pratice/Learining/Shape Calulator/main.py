import math
s = input(" What do you want to solve P = perimeter , A = Area, V = Volume: ")
if s == "A":
    shape = input("C= Circle, T = Triangle, Q = Quadrilateral: ")
    if shape == "C":
        W = input ("D = Diameter, R = Raduis, C = Circumfrence: ")
        if W == "D":
            diameter = input("What is the dimeter of a Cirlce: ")
            diameter = (float(diameter))
            Area = (math.pi *pow(diameter,2))/4
            Area_rounded = round(Area)
            print(f"The Area of this Cirlce is {Area} units² ")
            print(f"The Area of this Cirlce rounded is {Area_rounded} units² ")
            Done = input("Press Enter When You Are Done: ")
        elif W == "R":
            raduis = input("What is the Raduis of the Cirlce: ")
            raduis = float(raduis)
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

    elif shape == "T":
        h = float(input("The Heigth of the Triangle: "))
        b = float(input("The base of the Triangle: "))

        area = 1/2 * (h*b)
        Area_rounded = round(area)
        print(f"The Area of the Traingle is {area} units²")
        print(f"The Area of the Traingle is {Area_rounded} units²")
        Done = input("Press Enter When You Are Done: ")
    elif shape == "Q":
        Quad = input("K = Kite, T = Trapzoid, P = Parllogram: ")
        if Quad == "K" :
            d_1 = input("Length of Diagonal 1: ")
            d_2 = input("Length of diagonal 2: ")
            d_1 = float(d_1)
            d_2 = float(d_2)
            area = ((d_1*d_2)/2)
            Area_rounded = round(area)
            print(f"The area of the Kite is {area} unit² ")
            print(f"The area of the Kite is {Area_rounded} unit² ")
            Done = input("Press Enter When You Are Done: ")
        elif Quad == "T":
            l_1 = input("What is the Length of The Top Side: ")
            l_2 = input("What is the Length of The Bottom Side: ")
            h = input("The Length of heigth of the Trapezoid: ")
            l_1 = float(l_1)
            l_2 = float(l_2)
            h = float(h)
            Area = (((l_1 + l_2)/2)*h)
            Area_rounded = round(Area)
            print(f"The area of the Trapezoid is {Area} unit² ")
            print(f"The area of the Trapezoid is {Area_rounded} unit² ")
            Done = input("Press Enter When You Are Done: ")
        elif Quad == "P":
            S_1 = input("Length of Side 1: ")
            S_2 = (input("Length of Side 2: "))
            S_1 = float(S_1)
            S_2 = float(S_2)
            a = S_1 * S_1
            a_r = round(a)
            print(f"The area of the Parllogram is {a} unit² ")
            print(f"The area of the Parllogram is {a_r} unit² ")
            Done = input("Press Enter When You Are Done: ")
elif s == "P":
    shape_1 = input("T = Triangle, Q = Quadrilateral, C = Circle: ")
    if shape_1 == "T":
        p = input("Missing Side (Y/N): ")
        if p == "N":
            S_1 = input("Length of Side 1: ")
            S_2 = input("Length of Side 2: ")
            b = input("Length of Base: ")
            S_1 = float(S_1)
            S_2 =float(S_2)
            b = float(b)
            perimeter = S_1 + S_2 + b
            perimeter_r = round(perimeter)
            print(f"The Perimeter of this Trianlge is {perimeter} units")
            print(f"The Perimeter of this Triangle {perimeter_r} units")
            input("Press Enter to Close: ")
        elif shape_1 == "Y":
            Y_1 = input(" Do you have the Length hypotenuse (Y/N): ")
            if Y_1 == "N":
                Side_1 = input("Length of Side One: ")
                Side_2 = input("Length of Side Two: ")
                Side_1 = float(Side_1)
                Side_2 = float (Side_2)
                Side_3 = (pow(Side_1,2)+pow(Side_2,2))
                Side_3 = math.sqrt(Side_3)
                perimeter = Side_3 + Side_2 + Side_1
                perimeter_r = round(perimeter)
                print(f"The Perimeter of the triangle is {perimeter} units")
                print(f"The Perimeter of the triangle is {perimeter_r} units rounded ")
                input("Press Enter to Close: ")
            elif Y_1 == "Y":
               side_missing = input("Is there another missing side (Y/N): ")
               if side_missing == "N":
                   Side_1 = input("Length of Side One: ")
                   Side_2 = input("Length of Side Two: ")
                   Side_3 = input("Length of Side Three: ")
                   Side_1 = float(Side_1)
                   Side_2 = float(Side_2)
                   Side_3 = float(Side_3)
                   perimeter = Side_3 + Side_2 + Side_1
                   perimeter_r = round(perimeter)
                   print(f"The Perimeter of the trangle is {perimeter} units")
                   print(f"The Perimeter of the Triangle is  {perimeter_r} units rounded")
                   input("Press Enter to Close: ")
               elif side_missing == "Y":
                   Side_1 = input("The Length of the No Missing Side: ")
                   Side_1 = float(Side_1)
                   Side_3 = input("The Length of the Hypotenuse: ")
                   Side_3 = float(Side_3)
                   Side_2 = math.sqrt(pow(Side_3,2)-pow(Side_1,2))
                   perimeter = Side_3 + Side_2 + Side_1
                   perimeter_r = round(perimeter)
                   print(f"The Perimeter of the triangle is {perimeter} units: ")
                   print(f"The Perimeter of the trianlge is {perimeter_r} units: ")
                   input("Press Enter to Close: ")

    elif shape_1 == "C":
        find = input("What do we have; R = Raduis, D = Diameter, A = Area: ")
        if find== "R":
            r_1 = input("The raduis of the Triangle: ")
            r_1 = float(r_1)
            circumference = math.pi*(r_1 * 2)
            c_round = round(circumference)
            print(f"The Circumfrence of the Circle is {circumference} units")
            print(f"The Circumfrence of the Circle is {c_round} units")
            input("Press Enter to Close: ")
        elif find == "D":
            cd_1 = input("The diameter of the circle: ")
            cd_1 = float(cd_1)
            circumference = math.pi*(cd_1 * 2)
            c_round = round(circumference)
            print(f"The Circumfrence of the Circle is {circumference} units")
            print(f"The Circumfrence of the Circle is {c_round} units when rounded")
            input("Press Enter to Close: ")
        elif find == "A":
            a = input("Area of the Circle")
            a = float(a)
            raduis = math.sqrt(a/math.pi)
            d = raduis*2
            circumference = d*math.pi
            print(f"The Circumfrence of the Circle is {circumference} units")
            print(f"The Circumfrence of the Circle is {circumference} units when rounded")
            input("Press Enter to Close: ")
if s == "V":
     e_shape = input("Prism, Sphere, Cube, C= Cone  ")
   
  