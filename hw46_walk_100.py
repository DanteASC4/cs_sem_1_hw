#Name: Dante Rivera
#Date: October 2018
#A turtle that walks randomly for 100 steps


import random
import turtle


bob = turtle.Turtle()
bob.speed('fastest')



for i in range(100):
  bob.right(random.randrange(0, 359, 1))
  bob.forward(10)

  