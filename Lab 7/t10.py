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
from functions import employee_payroll
# Constants

total, average = employee_payroll()

print("\nTotal payment:      ${:,.2f}".format(total))
print("Average payment:    ${:,.2f}".format(average))
