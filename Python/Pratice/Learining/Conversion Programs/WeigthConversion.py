print("Weigth Conversion Program")
unit = input("P = Pounds / KG = Kilogram: ")
if unit == "P":
    weigth = int(input("Wegith in pounds: "))
    Kilograms = weigth * 0.45359237
    print(f"You weigh {Kilograms} Kg")
    Kilograms_Round = round(Kilograms)
    print(f"You weigh {Kilograms_Round} Kg rounded")
    input("Press Enter to Close: ")
elif unit == "KG":
    weigth = int(input("How much Kilograms/KG to you weigh: "))
    pounds = weigth * 2.20462262
    pounds_r = round(pounds)
    print(f"You weigh {pounds} pounds")
    print(f"You weigh {pounds_r} pounds rounded")
    input("Press Enter to Close: ")