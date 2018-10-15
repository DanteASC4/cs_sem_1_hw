# Name:  Dante Rivera
# Date:  August 29th, 2018
# Asks for image name and output name, saves new cropped image displaying bottom left half of image


import matplotlib.pyplot as plt
from PIL import *


i_name = input('Enter the image name:   ')
o_name = input('Enter the output name:    ')


img = Image.open(i_name )
w, h = img.size
n = h/2
cropped_img = img.crop((0, n, w/2, h))
cropped_img.save(o_name)
