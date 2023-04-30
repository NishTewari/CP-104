'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-29"
-----------------------------------------------

'''
# Imports
from functions import meal_costs
# Constants

b_total, l_total, s_total, a_total = meal_costs()

print("""\nTotal:
Breakfast:    ${:.2f}
Lunch:        ${:.2f}
Supper:       ${:.2f}""" .format(b_total, l_total, s_total))

print("\nGrand total: ${:.2f}".format(a_total))
