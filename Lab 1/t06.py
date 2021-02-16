"""
------------------------------------------------------------------------
Calculating the user's pay with salary and bonus
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-16"
------------------------------------------------------------------------
"""

#User Input 
print("Hello User, today we will calculate your total pay at your workplace!")
salary = int(input("What is your job salary? "))
bonus  = int(input("What is the bonus you receive from work? "))

#Calculate the user's overall pay
pay = salary + bonus 

#Print the overall pay for the user
print('Calculating your overall pay. Your pay is', pay)