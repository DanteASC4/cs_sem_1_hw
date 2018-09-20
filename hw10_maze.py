#Name: Dante Rivera
#Date: August 27th, 2018
#This program draws a maze with turtle



#Importing turtle module
import turtle

#Creating a turtle and naming it
dat_t = turtle.Turtle()


# For i = 10, 20, 30,... ,250:
#        Walk forward i steps
#        Turn left 90 degrees
i = 0
while i < 250:
    i += 10
    dat_t.forward(i)
    dat_t.left(90)
