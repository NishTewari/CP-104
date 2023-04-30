'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-28"
-----------------------------------------------

'''
# Imports
from functions import population_growth
# Constants

target = int(input("Target population: "))
current = int(input("Current population: "))
rate = (float(input("Growth rate (%): ")))  

years = population_growth(target, current, rate)

print("\nYears to reach target: {}".format(years))
