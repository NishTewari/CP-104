"""
------------------------------------------------------------------------
A simple program to calculate the monthly payment for a mortgage.
Mortgage equation m = p [(i(1 + i)^n) / (i + i)^n - 1]
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-15"
------------------------------------------------------------------------
"""

#Variables 
principal_amount = float(input("Mortgage Principal ($): "))
num_years = int(input("Number of years: "))
interest_rate = float(input("Yearly interest rate (%): "))

#set interest_rate to decimal form 
monthly_interest_rate = (interest_rate / 100) / 12  

#calculate the number of months 
months = num_years * 12

#Below will be the formula to calculate the mortgage split in two parts (numerator / denominator) 
mortgage_numerator = monthly_interest_rate * ((1 + monthly_interest_rate)**months)
mortgage_denominator = ((1 + monthly_interest_rate)**months) - 1

#Divide the numerator(top part of equation) by the denominator(bottom half of the eqaution)
divided_mortgage = mortgage_numerator / mortgage_denominator
#multiply the principal amount 
final_mortgage = principal_amount * divided_mortgage

print("\nThe monthly payments are: ${:,.2f}".format(final_mortgage))

