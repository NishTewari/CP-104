'''
-----------------------------------------------
Question 4 
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-06-30"
-----------------------------------------------

'''

from a6_functions import is_prime

num = int(input("Enter a positive integer: "))

while(num <= 0):
    num = int(input("\nEnter a positive integer: "))

prime = is_prime(num)

if(prime == False):
    print("\n{} is a prime number".format(num))
else:
    print("\n{} is not a prime number".format(num))
    
