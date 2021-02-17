'''
-----------------------------------------------
Calculate future population given various 
factors
-----------------------------------------------
Author: Nish Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
# Imports
from functions import population

#Variables
size = int(input("Current population: "))
births = int(input("Average seconds between births: "))
deaths = int(input("Average seconds between deaths: "))
immigrants = int(input("Average seconds between immigrations:  "))
years = int(input("Years in the future: "))

#Call the function 
new_size = population(size, births, deaths, immigrants, years)

#Print the new population back to the user 
print("\nThe new population will be {:,d}".format(new_size))
