temp_unit = input("Enter the Unit of Mesurement Celsius or Fahrenheit (C/F): ")
if temp_unit == "C":
    tempture = input("Enter the Tempture in Celsius: ")
    tempture = float(tempture)
    f_temp = (tempture *1.8) +32
    print(f"Tempture in Fahrenheit is {f_temp}")
    input("Enter to Close: ")
if temp_unit == "F":
    tempture = input("Enter the Tempture in Fahrenheit: ")
    tempture = float(tempture)
    c_temp = (tempture - 32)/1.8
    print(f"Tempture in Celsius is {c_temp}")
    input("Enter to Close: ")