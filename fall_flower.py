#Name: Dante Rivera
#Date: August 27th, 2018
#Creates a flower-shaped pattern with turtle when run

#Importing turtle module
import turtle

#Creating a turtle and naming it
dat_t = turtle.Turtle()


# Repeat 36 times:
#        Walk forward 100 steps
#        Turn left 145 degrees
#        Walk forward 10 steps
#        Turn right 90 degrees
#        Walk forward 10 steps
#        Turn left 135 degrees
#        Walk forward 100 steps
#
#
for i in range(36):
    dat_t.forward(100)
    dat_t.left(145)
    dat_t.forward(10)
    dat_t.right(90)
    dat_t.forward(10)
    dat_t.left(135)
    dat_t.forward(100)
