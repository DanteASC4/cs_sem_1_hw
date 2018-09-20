#Name: Dante Rivera
#Date: August 28th, 2018
#This program takes a user given hexadecimal and prints a turtle the given color


#importing turtle
import turtle

# Creating turtle
dat_t = turtle.Turtle()

# Turtle shape
dat_t.shape('turtle')

# Get hexadecimal color value
hex = input('Enter a hexadecimal color:         ')

# Change color accordingly
dat_t.color(hex)
