"""
------------------------------------------------------------------------
A simple program that multiplies two fractions together using the 
formula r = n1/d1 x n2/d2 
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-15"
------------------------------------------------------------------------
"""
#User defined variables 
first_numerator =  int(input("First numerator: "))
first_denominator = int(input("First denominator: "))
second_numerator = int(input("Second numerator: "))
second_denominator = int(input("Second denominator: "))

#fraction multiplication formula 
product = (first_numerator/first_denominator) * (second_numerator/ second_denominator)

#final print statement to showcase the answer
print("Product: {0:.4f}".format(product))
