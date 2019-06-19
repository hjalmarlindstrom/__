import turtle

myPen = turtle.Turtle()
screen = turtle.Screen()
screen.setworldcoordinates(-10, -50, 10, 50)
myPen.speed(0)

def drawAxis():
    myPen.penup()
    myPen.goto(-10, 0)
    myPen.pendown()
    myPen.goto(10, 0)

    myPen.penup()
    myPen.goto(0, -50)
    myPen.pendown()
    myPen.goto(0, 50)

def first(a, b):
    myPen.penup()
    for x in range(-10, 11):
        y = a * x + b
        myPen.goto(x, y)
        myPen.pendown()

    myPen.penup()
    myPen.goto(-10, 10)


drawAxis()
for i in range(1000):
    myPen.color('red')
    first(i/2, 0)
    myPen.color('blue')
    first(-i/2, 0)
    
