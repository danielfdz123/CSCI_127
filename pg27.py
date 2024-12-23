#Daniel Andres Fernandez
#daniel.fernandez16@myhunyer.cuny.edu
#March 10, 2022
#This program plots a graph based on population of a borough inputed by the user

import matplotlib.pyplot as plt                     #Load in libraries
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)      #Reads in information
boro = input("Enter borough name: ")                #User inputs borough name
out = input("Enter output file name: ")             #User inputs name out output file
pop['Fraction'] = pop[boro]/pop['Total']            #Gathers fraction of borough pop/total pop

pop.plot(x = 'Year', y = 'Fraction')                #Plots the fraction in a graph
fig = plt.gcf()
fig.savefig(out)                                    #Saves the graph under the name that the user inputed as 'out'

plt.show()                                          #Shows grapha
plt.imshow()
