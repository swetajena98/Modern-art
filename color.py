#!/bin/python3

from turtle import *
from random import *
def randomcolour():
  red = randint(0,255)
  blue = randint(0,255)
  green = randint(0,255)
  color(red,blue.green)
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
  randomcolour()
  randomplace()
  randomheading()
  stamp()
 
