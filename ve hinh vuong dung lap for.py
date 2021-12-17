#hình vuông
import turtle
turtle.bgcolor('light blue')
t=turtle.Turtle()
t.penup()
t.goto(-200,-200)
t.pendown()
t.pensize(3)
t.pencolor('red')
t.fillcolor('green')
t.begin_fill()
for i in range (4):
    t.fd(190)
    t.lt(90)
t.end_fill()
turtle.done()