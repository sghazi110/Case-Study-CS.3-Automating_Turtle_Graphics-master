#double smiley face
#jump function
def jump(t,x,y):
    'easy to jump to another point instead of penup nad pendown'
    t.penup()
    t.goto(x,y)
    t.pendown()
import turtle
s=turtle.Screen()
t=turtle.Turtle()
def smileyface(t,x,y):
    'this create a smiley face'
    t.pensize(3)
    t.setheading(0)
    jump(t,x,y)
    t.circle(100)
    jump(t,x+35,y+120)
    t.dot(25)
    jump(t,x-35,y+120)
    t.dot(25)
    jump(t,x-60.62,y+65)
    t.setheading(-60)
    t.circle(70,120)
smileyface(t,-100,100)
smileyface(t,150,100)
