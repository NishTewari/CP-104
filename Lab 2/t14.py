"""
------------------------------------------------------------------------
A program that asks the user how many servings of Mac and Cheese they 
want to make, and print out the resulting ingredient list.
To create six servings of Mac and Cheese, you require the following 
ingredients:

milk: 4 cups
butter: 8 tablespoons
flour: 0.5 cups
salt: 2 teaspoons
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-17"
------------------------------------------------------------------------
"""
#CONSTANTS
MILK = 4
BUTTER = 8 
FLOUR = 0.5
SALT = 2

#Variables 
user_servings = int(input("Enter servings of Mac & Cheese: "))

#Calculating the amount of ingreidents needed to fulfil the servings requested by user 
milk_needed = (MILK / 6) * user_servings
butter_needed = (BUTTER / 6) * user_servings
flour_needed = (FLOUR / 6) * user_servings
salt_needed = (SALT / 6) * user_servings


print("""
{} servings of Mac & Cheese requires:
Milk (cups): {:.2f}
Butter (tablespoons): {:.2f}
Flour (cups): {:.2f}
Salt (teaspoons): {:.2f}""".format(user_servings, milk_needed, butter_needed, flour_needed, salt_needed))


