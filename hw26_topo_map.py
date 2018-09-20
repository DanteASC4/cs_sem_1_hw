# Name:  Dante Rivera
# Date:  August 28th, 2018
# Takes elevation data of NYC and displays using the default color map


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

# greater than 6 feet and less than or equal 20 feet above sea level the color grey
#
#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = .25     #Set the blue channel to 100%
        elif elevations[row,col] % 10 == 0:
         floodMap[row,col,0] = 0
         floodMap[row,col,1] = 0
         floodMap[row,col,2] = 0
        else:
         floodMap[row,col,0] = .5
         floodMap[row,col,1] = .5
         floodMap[row,col,2] = .5

#Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

#Display the plot:
plt.show()

#Save the image:
plt.imsave('topo.png', floodMap)
