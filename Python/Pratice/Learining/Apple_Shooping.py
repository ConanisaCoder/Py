print("You have Now entered the Apple Store: ")
print("What would you like to buy at Apple")
print("Choose Items to Buy")
items = ["iPhone 16","iPhone 15","Apple Watch Series 10","Apple Vison Pro","AirPods 4","Airpods Max", "AirTag"]
price = [1500,1100,550,5000,250,780,40]
shooping_list = ""
total = 0
Index = 0
print("These are the items for purchase today what would like to buy as items")
for i in range(0,7,1):
    if Index < 7:
        print("Item " + str(i) + ": " + items[Index] +" $" + str(price[Index]))
    else:
        print(items[Index] +" $" + str(price[Index]))
    Index += 1
item_buy = int(input("How many items to buy: "))
for i in range(0,item_buy,1): 
    item_buying = int(input("What Item number are you buying: "))
    if item_buying > 7:
        item_buying = 7
    total += price[item_buying]
    shooping_list += items[item_buying] + "\n"
total += total * 0.13
print(f"Items Bougth: \n{shooping_list}")
print(f"Your total is $ {total}")