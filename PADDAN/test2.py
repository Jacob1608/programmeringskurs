import turtle
turtle.bgcolor("black")

teppo = turtle.Turtle()
teppo.speed(100)

farger = ['red', 'blue', 'green', 'black', 'yellow']
for i in range(80):
    for f in farger:
        teppo.color(f)
        teppo.circle(50)
        teppo.left(10)
        teppo.backward(10)
