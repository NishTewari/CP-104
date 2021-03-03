'''
-----------------------------------------------
A program to calculate the total cost of three
clothing items. 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Variables
sweatband_cost = float(input("Enter cost of sweatband:$ "))  # User input of the sweatband cost
pants_cost = float(input("Enter cost of pants:$ "))  # User input of the pants cost
jacket_cost = float(input("Enter cost of jacket:$ "))  # User input of the jacket cost

# calculate total cost by adding all three costs together 
total_cost = sweatband_cost + pants_cost + jacket_cost  

# Print a listing of all cost and its total cost
print("Clothes", "     Cost")  
print("Sweatband     ${:6.2f}" .format(sweatband_cost))
print("Pants         ${:6.2f}".format(pants_cost))
print("Jacket        ${:6.2f}".format(jacket_cost))
print("Total         ${:6.2f}".format(total_cost))
