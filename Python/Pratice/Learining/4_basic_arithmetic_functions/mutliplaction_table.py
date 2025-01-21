v = float(input("What do you want to mutiply: "))
e = int(input("What integer do want to start at: "))
r = int(input("What number do you want to go to: "))
for i in range(e,r+1,1):
    d = v*i
    print(f"{v} x {i} = {d}")