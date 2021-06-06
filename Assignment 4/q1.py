'''
-----------------------------------------------
Assignment Four, Question One
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-15"
-----------------------------------------------

'''
# Imports
from q1_functions import calc_federal_tax, calc_prov_tax

# User inputs their income
income = int(input("Enter your income: $"))

# Using the function, it calculates the federal tax for the user 
(federal_tax_total) = calc_federal_tax(income)

# Using the function, it calculates the stae tax for the user 
(state_income_tax) = calc_prov_tax(income)

print("""\nYour total tax liability is: $ {:.0f}
[details federal tax: $ {:.0f}, state tax: $ {:.0f}]""".format((federal_tax_total + state_income_tax), federal_tax_total, state_income_tax))
