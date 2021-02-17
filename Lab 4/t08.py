'''
-----------------------------------------------
Calculate the pre commission and post 
commission of computers sold at a store. 
-----------------------------------------------
Author: Nish Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Imports 
from functions import computer_costs

#Variables 
computer_cost = float(input("Cost of each computer: $"))
computers_bought = int(input("Number of computers bought: "))
commission_percent = float(input("Wholesaler commission: % "))

#Call the function 
pre_commission_cost, total_cost = computer_costs(computer_cost,computers_bought, commission_percent)

#Print the pre commission and total amount back to user
print("\nCost of Computers (no commission)    ${:6,.2f}".format(pre_commission_cost))
print("Cost of computers (total):           ${:6,.2f}".format(total_cost))