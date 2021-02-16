"""
------------------------------------------------------------------------
Write and test a program that prompts the user to enter the number of 
flyers and the number of volunteers, and prints the number of flyers 
per volunteer and the number of flyers left over.
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-16"
------------------------------------------------------------------------
"""
#Variables 
num_flyers = int(input("Number of flyers: "))
num_volunteers = int (input("Number of volunteers: "))

# Distributing the flyers to the volunteers equally using the integer division operator. 
divided_equally = num_flyers // num_volunteers

#finding the # of flyers leftover using the modulus operator 
flyers_leftover = num_flyers % num_volunteers

print("Flyers per volunteer: {:.0f}".format(divided_equally))
print("Flyers left over: {:.0f}".format(flyers_leftover))