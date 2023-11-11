#Daniel Andres Fernandea
#daniel.fernandez16@myhunter.cuny.edu
#March 1, 2022
#This program loads an image, displays it, and then creates, display and saves a new image that has only the red channel displayed.

import matplotlib.pyplot as plt    #Import the packages for images and arrays:
import numpy as np

img = plt.imread('csBridge.png')         #Read in image from csBridge.png

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0          #Set the red channel to 0
img2[:,:,1] = 0          #Set the green channel to 0
plt.show()

plt.imsave('blueH.png', img2)  #Save the image we created to the file: blueH.png
plt.show()
