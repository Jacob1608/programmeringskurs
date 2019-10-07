import turtle
turtle.bgcolor("black")

teppo = turtle.Turtle()
teppo.speed(100)

print ("Hurdan rektangel får det vara?")

width = int(input("Bredd?"))
length = int(input("Längd?"))
color = input("Färg?")

if color == "Röd":
    teppo.pencolor("red")
    
else:
    teppo.pencolor("blue")
        

teppo.goto(0,0)
teppo.forward(length)
teppo.left(90)
teppo.forward(width)
teppo.left(90)
teppo.forward(length)
teppo.left(90)
teppo.forward(width)

input()