import turtle
side = int(input("Side length px:"))
window = turtle.Screen()
s = turtle.Turtle()

for i in range(0,4,1):
    s.forward(side)
    s.right(90)