#Daniel Andres Fernandez
#daniel.fernandez16@myhunter.cuny.edu
#March 4, 2022
#This program print out a grid determined by the user, that alternates in red/white stripes

import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter size: "))
out = input("Enter output file: ")

img = np.zeros( (num,num,3) )
img[::2,:,1:] = 0

plt.imshow(img)
plt.show()
plt.imsave(out, img)
