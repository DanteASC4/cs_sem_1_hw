import random
import turtle


bob = turtle.Turtle()
bob.speed('fastest')

  # bob.right(random.randrange(0, 359, 60))
  # bob.forward(10)

for i in range(1000):
  bob.right(random.randrange(0, 359, 60))
  bob.forward(10)
  bob.right(60)
  bob.forward(5)
  bob.right(60)
  
  