'''
-----------------------------------------------
Calculate the product of two fractions and 
calculating the decimal form of the fraction 
-----------------------------------------------
Author: Nish Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Imports 
from functions import fraction_product

#Variables 
num1 = int(input("Enter numerator of fraction 1: "))
den1 = int(input("Enter denominator of fraction 1: "))
num2 = int(input("Enter numerator of fraction 2: "))
den2 = int(input("Enter denominator of fraction 2: "))


#Call the function 
num, den, product = fraction_product(num1, den1, num2, den2)

#Print the total amount back to user
print("\nProduct =  {}/{} ".format(num,den))
print("Decimal =   {:.2f}".format(product))