"""
------------------------------------------------------------------------
Write a program that asks a user for the cost of a meal and the 
percentages for the tax and tip, and prints a bill.
All three values should be floats.
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-16"
------------------------------------------------------------------------
"""
#Variables
food_charge = float(input("Food Charge: $"))
sales_tax = float(input("Sales Tax in (%): "))
meal_tip = float(input("Tip in (%): "))

#calculating the tax 
applied_tax = (sales_tax / 100) * food_charge

#calculating the tip percentage
applied_tip = (meal_tip / 100) * food_charge

#calculating the total bill
total_bill = food_charge + applied_tax + applied_tip

print("""
Cost of meal:
Subtotal: ${:6.2f}
     Tax: ${:6.2f}
     Tip: ${:6.2f}
-----------------    
   Total: ${:6.2f}""".format(food_charge, applied_tax, applied_tip, total_bill))