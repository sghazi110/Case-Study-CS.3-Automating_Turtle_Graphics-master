def jump(t,x,y):
    'easy to jump to another point instead of penup nad pendown'
    t.penup()
    t.goto(x,y)
    t.pendown()
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def olympic(t):
    t.pensize(3)
    jump(t,0,0)
    t.setheading(0)
    t.circle(100)
    jump(t,-220,0)
    t.circle(100)
    jump(t,220,0)
    t.circle(100)
    jump(t,-110,-100)
    t.circle(100)
    jump(t,110,-100)
    t.circle(100)
olympic(t)
