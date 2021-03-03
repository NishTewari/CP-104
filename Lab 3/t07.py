'''
-----------------------------------------------
A program to calculate the total cost of a full
day of eating outside for all 3 main courses
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Variables
breakfast_cost = float(input("Enter cost of breakfast: $"))  
lunch_cost = float(input("Enter cost of lunch: $"))  
supper_cost = float(input("Enter cost of supper: $"))  

# calculate total cost by adding all three costs together 
total_cost = breakfast_cost + lunch_cost + supper_cost

# Print a listing of all cost and its total cost
print("Meal", "         Cost")  
print("Breakfast     ${:6.2f}" .format(breakfast_cost))
print("Lunch         ${:6.2f}".format(lunch_cost))
print("Supper        ${:6.2f}".format(supper_cost))
print("Total         ${:6.2f}".format(total_cost))
