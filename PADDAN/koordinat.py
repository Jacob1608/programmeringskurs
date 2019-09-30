import turtle

teppo = turtle.Turtle()
teppo.penup()
teppo.pencolor("black")

while open:
    axelX = input ("Var skall cirkeln vara på linje X?")
    axelY = input ("Var ska cirkeln vara på linje Y?")

    teppo.goto (int(axelX), int (axelY))
    teppo.pendown
    teppo.circle(50)
    
teppo.done()