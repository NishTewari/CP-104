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
from functions import budget
# Constants

available = float(input("Monthly budget: $"))

expense, balance, status = budget(available)

print("\nTotal expenses: ${:.2f}".format(expense))
print("{}: ${:.2f}".format(status, balance))
