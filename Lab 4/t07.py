'''
-----------------------------------------------
Calculate the total value of a set of coins in 
dollars. 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------
'''
#Imports 
from functions import total_change

#Variables 
nickels = int(input("Enter number of nickels: "))
dimes = int(input("Enter number of dimes: "))
quarters = int(input("Enter number of quarters: "))
loonies = int(input("Enter number of loonies: "))
toonies = int(input("Enter number of toonies: "))

#Call the function 
total = total_change(nickels, dimes, quarters, loonies, toonies)

#Print the total amount back to user
print("\nTotal amount: ${:.2f}".format(total))