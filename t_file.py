# Name:  Dante Rivera
# Date:  August 28th, 2018
# Fraction of Children in shelters from 2013
#
 import pandas as pd
import matplotlib.pyplot as plt
 f_name = input('Enter the file name:  ')
o_name = input('Enter the output file name:  ')
 homeless = pd.read_csv(f_name + ".csv")
 homeless['Fraction'] = homeless["Total Children in Shelter"]/homeless['Total Individuals in Shelter']
 homeless.plot(x = "Date of Census", y = "Fraction")
plt.show()
 fig = plt.gcf()
fig.savefig(o_name + '.png')
