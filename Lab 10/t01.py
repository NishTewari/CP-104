'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-11-19"
-----------------------------------------------

'''
# Imports
from functions import customer_record
# Constants

fv = open("customers.txt", "r")

print("Find record n")

n = int(input("\nEnter a record number: "))

result = customer_record(fv, n)

print(result)

fv.close()
