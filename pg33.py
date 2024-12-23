#Daniel Andres Fernandez
#daniel.fernandez16@myhunter.cuny.edu
#March 17, 2022
#This program prints the lower left quarter of an image specified by the user

import matplotlib.pyplot as plt
import numpy as np

image = input("Enter input file: ")
output =  input("Enter output file: ")

img= plt.imread(image)
height = img.shape[0]
width = img.shape[1]

img2 = img[height//2:, :width//2]

plt.imsave(output,img2)
