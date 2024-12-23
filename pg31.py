#Daniel Andres Fernandez
#daniel.fernandez16@myhunter.cuny.edu
#March 10, 2022
#This program plots the population of a shelter overtime

import matplotlib.pyplot as plt
import pandas as pd

input_file=input("Enter name of input file:")
out = input("Enter name of output file:")

pop=pd.read_csv(input_file)

pop["Fraction Children"] = pop["Total Children in Shelter"]/pop["Total Individuals in Shelter"]

pop.plot(x="Date of Census",y="Fraction Children")

fig=plt.gcf()
fig.savefig(out)

