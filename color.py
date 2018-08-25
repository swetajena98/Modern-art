#!/bin/python3

from turtle import *
from random import *
shape("turtle")
color(200,0,200)
def randomplace():
  penup()
  x = randint(-100,100)
  y = randint(-100,100)
  goto(x,y)
  pendown()
def randomheading():
  number = randint(1,360)
  setheading(number)
 
for i in range(20):
  
  randomplace()
  randomheading()
  stamp()
 