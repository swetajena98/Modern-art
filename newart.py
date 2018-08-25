#!/bin/python3

from turtle import *
from random import *
shape("turtle")
speed(10)
def randomcolor():
  red = randint(0,255)
  blue = randint(0,255)
  green = randint(0,255)
  color(red,green,blue)
def randomplace():
  penup()
  x = randint(-100,100)
  y = randint(-100,100)
  goto(x,y)
  pendown()
def randomheading():
  number = randint(1,360)
  setheading(number)
 
clear()
setheading(0)
def drawrectangle():
  randomcolor()
  randomplace()
  hideturtle()
  length = randint(5,100)
  height=randint(5,100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()
for i in range(10):
    drawrectangle()
