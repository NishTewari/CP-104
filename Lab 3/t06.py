'''
-----------------------------------------------
A program to find the total cost of an item 
based on the quantity
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Variables 
cost_num = float(input("Please enter a cost number:"))  # User input of the cost Number
quantity_num = int(input("Please enter a quantity number: "))  # User Input of the number of quantity 

# Calculate total cost by multiplying cost by the quantity 
total_cost = cost_num * quantity_num  

#print back to the user
print("Given a cost of ${:.2f} and a quantity of {} the total is ${:.2f}".format(cost_num, quantity_num, total_cost))  
