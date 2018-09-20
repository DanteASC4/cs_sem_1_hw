#Name:  Dante Rivera
#Date:  August 28th, 2018
#This program loads an image, displays it, and then creates, displays, and saves a new image that has only the red channel displayed.


img = input('Enter an image name with the file ending:    ')

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


img = plt.imread(img)   #Read in image from csBridge.png
plt.imshow(img)		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0          #Set the green channel to 0
img2[:,:,1] = 0          #Set the blue channel to 0


plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)
bimg = input('Enter a name for the new file with a file ending:   ')
plt.imsave(bimg, img2)  #Save the image we created to the file: reds.png
