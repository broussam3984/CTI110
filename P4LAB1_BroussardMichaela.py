import turtle

screen = turtle.Screen()
screen.bgcolor("lightyellow")

t = turtle.Turtle()
t.color("blue")
t.pensize(3)

t.penup()
t.goto(-50, -50)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-50, 50)
t.pendown()

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

turtle.done()    