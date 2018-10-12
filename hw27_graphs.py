# Name:  Dante Rivera
# Date:  August 28th, 2018
# Takes a user given borough and creates an image of a graph based off of data



#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

burrow = input('Enter a borough name:   ')
file = input('Enter a file name:    ')

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[burrow]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(file)
