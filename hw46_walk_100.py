import random
import turtle


bob = turtle.Turtle()
bob.speed('fastest')



for i in range(100):
  bob.right(random.randrange(0, 359, 1))
  bob.forward(10)

  