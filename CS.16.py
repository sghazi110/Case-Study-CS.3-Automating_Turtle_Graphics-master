#CS.16 (spiral)
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def square(l,ang):
     for i in range(1,5):
        t.forward(l)
        t.right(90)
def spiral(l,ang,mul):
    for i in range(1,5):
        t.forward(l)
        t.right(90)
    t.speed(400)
    t.pensize(3)
    for i in range(1,mul+1):
        square(l,ang)
        t.right(10)
spiral(50,90,37)
