import turtle
turtle.bgcolor("black")

teppo = turtle.Turtle()
teppo.forward(100)
teppo.speed(500)


for i in range(100):
    teppo.pencolor("blue")
    teppo.pensize(1)
    teppo.circle(75)
    teppo.left(5)
    teppo.backward(5)
    
teppo.penup()
teppo.goto(-100, -50)
teppo.pendown()

for i in range(100):
    teppo.pencolor("red")
    teppo.pensize(1)
    teppo.circle(75)
    teppo.left(5)
    teppo.backward(5)
    
teppo.penup()
teppo.goto(50, 100)
teppo.pendown()

for i in range(100):
    teppo.pencolor("yellow")
    teppo.pensize(1)
    teppo.circle(75)
    teppo.left(5)
    teppo.backward(5)

teppo.penup()
teppo.goto(200, -50)
teppo.pendown()

for i in range(100):
    teppo.pencolor("green")
    teppo.pensize(1)
    teppo.circle(75)
    teppo.left(5)
    teppo.backward(5)

teppo.penup()    
teppo.speed(1)
teppo.goto(300, 300)
teppo.write("WOW! VILKET MÖNSTER!")

