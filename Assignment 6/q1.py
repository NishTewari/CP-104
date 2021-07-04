'''
-----------------------------------------------
Assignment Six Question One
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2019-10-26"
-----------------------------------------------
'''
from a6_functions import calc_profit

# User input of investment amount
principal = float(input("PLease enter your investment amount: "))

# User input of the number of years
year = int(input("Please enter number of years: "))

# Calls the Function!
value = calc_profit(principal, year)
