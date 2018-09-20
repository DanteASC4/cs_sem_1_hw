#Name: Dante Rivera
#Date: August 27th, 2018
#This program asks the user for 5 numbers, and draws using turtle and the given values


#Importing turtle module
import turtle

#Creating a turtle and naming it
dat_t = turtle.Turtle()


n1 = int(input('Enter a number:   '))
n2 = int(input('Enter a number:   '))
n3 = int(input('Enter a number:   '))
n4 = int(input('Enter a number:   '))
n5 = int(input('Enter a number:   '))


dat_t.left(n1)
dat_t.forward(100)
dat_t.left(n2)
dat_t.forward(100)
dat_t.left(n3)
dat_t.forward(100)
dat_t.left(n4)
dat_t.forward(100)
dat_t.left(n5)
dat_t.forward(100)


turtle.mainloop()
