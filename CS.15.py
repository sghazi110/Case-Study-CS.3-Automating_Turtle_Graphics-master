#CS.15(grid)
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def grid(m,n):
    x=0
    y=0
    for i in range(m):
        for j in range(n):
            t.penup()
            t.goto(x,y)
            t.pendown()
            box()
            x+=75
        y-=75
        x=0
        t.penup()
        t.goto(x,y)
        t.pendown()

            
def box():
    for i in range(4):
        t.forward(75)
        t.right(90)
grid(2,2)
