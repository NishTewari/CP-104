'''
-----------------------------------------------
Lab Five, Task 12
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-08"
-----------------------------------------------
'''
from functions import pay_raise

status = input("Status: ")
years = int(input("Years: "))
salary = float(input("Salary: "))

new_salary = pay_raise(status, years, salary)

print("New Salary: ${:,.2f}".format(new_salary))
