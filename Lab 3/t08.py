'''
-----------------------------------------------
A program to calculate the total cost of three
building materials 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Variables
dirt_amount = float(input("Enter amount of dirt (m^3): "))  
gravel_amount = float(input("Enter amount of gravel (m^3): "))  
sand_amount = float(input("Enter amount of sand (m^3): ")) 

# calculate total amount by adding all three amounts together 
total_amount = dirt_amount + gravel_amount + sand_amount  

# Print a listing of all cost and its total cost
print("Material","     Cubic Metres")  
print("Dirt           {:6.1f}".format(dirt_amount))
print("Gravel         {:6.1f}".format(gravel_amount))
print("Sand           {:6.1f}".format(sand_amount))
print("Total          {:6.1f}".format(total_amount))
