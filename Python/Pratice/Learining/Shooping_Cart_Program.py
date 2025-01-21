item = (input(" What item would you like to boy?: "))
price = (float(input("What is the price?: ")))
item_count = (int(input("How many are you buying: ")))
total = price * item_count

print(f"You are buying {item_count} {item} it will cost {total} dollars")