"""
------------------------------------------------------------------------
A simple program to calculate the total earnings for a dog grooming 
business. 
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-15"
------------------------------------------------------------------------
"""
#CONSTANTS --> Business Pricing
LARGE_DOG_COST = 75.00
SMALL_DOG_COST = 50.00 

#Ask the Business owner on how manys were groomed for the day? 
large_dog_groomed = int(input("Number of large dogs groomed: "))
small_dog_groomed = int(input("Number of small dogs groomed: "))

#calculate how much the business made for the day 
#multiply the number of large dogs groomed by its pricing. (Same with the small dogs) and add them together 
total_earned = (large_dog_groomed * LARGE_DOG_COST) + (small_dog_groomed * SMALL_DOG_COST)

#print a final total earning statement 
print("Total earned for the day: ${:,.2f}".format(total_earned))

