'''
-----------------------------------------------
Assignment Two, Question Two
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-02"
-----------------------------------------------

'''
#User input to retrieve information on the user's principal amount, interest rate,....
principal = float(input("Enter Principal Amount: ")) 
interest = float(input("Enter Annual Rate of Interest (decimal): "))   
years = float(input("Enter the Number of Years: "))    
compound = float(input("Enter the Compound Interest per year: "))   

#Calculate the final amount using the following compound interest formula
final_amount = principal * (1 + interest / compound) ** (compound * years) 

#Print a sentence stating the user's balance of the final amount 
print("\nBalance: ${:.2f}".format(final_amount)) 
