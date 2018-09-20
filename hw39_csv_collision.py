#Name: Dante Rivera
#Date: August 30th 2018
#Lists the top three contributing factors for the primary vehichle of collisions

#Import pandas for reading and analyzing CSV data:
import pandas as pd



c_f = input('Enter CSV file name: ')         #Name of the CSV file
att = "CONTRIBUTING FACTOR VEHICLE 1"
reason = pd.read_csv(c_f)     #Read in the file to a dataframe
print("Top 3 contributing factors for collisions:")
print(reason[att].value_counts()[:10]) #Print out the dataframe
