#CSci 127 Teaching Staff
#February 2018
#A template for a program that draws nested triangles
#Modified by: Dante Rivera

import turtle

dat_t = turtle.Turtle()
dat_t.speed('fastest')

n = int(input('Enter a length:   '))



def nestedTriangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length/2)


nestedTriangle(dat_t, n)
