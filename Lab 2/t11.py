"""
------------------------------------------------------------------------
A program that asks the user to enter the projected amount of total 
sales and then displays the profit that is made from that amount.
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-16"
------------------------------------------------------------------------
"""
#Constant 
ANNUAL_PERCENT = 18 

#Variables 
annual_sales = float(input("Enter projected annual sales: $"))

#calculate the projected sales with the given percentage 
projected_sales = annual_sales * (ANNUAL_PERCENT/100)

#print the projected profit back to the user
print("\nThe projected profit on sales of ${:,.2f} is ${:,.2f}".format(annual_sales, projected_sales))