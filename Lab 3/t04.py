'''
-----------------------------------------------
A program that calculates the discount on a 
user given number and percentage
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Variables
user_number = float(input("Enter number: "))
user_percent = float(input("Enter percent: "))

#calculate the discount 
discount = (user_percent / 100) * user_number

#print the discount back to the user 
print("\nA {:.1f} percent discount on {:.0f} is {:.1f}".format(user_percent, user_number, discount))
