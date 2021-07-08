'''
-----------------------------------------------
Assignment Six Functions
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-08"
-----------------------------------------------
'''
import math

# Question 1
def calc_profit(principal, year):
    """
    ------------------------------------------------------
    Calculates and displays the value of growth per year
    Use: value = calc_profit(principal,year)
    ------------------------------------------------------
    Parameters:
        principal - amount of money to invest in the house 
        (int or float)
        year - number of years of investment(int)
    Returns:
        value - value of growth per year(float)
    ------------------------------------------------------
    """ 
    
    INTEREST_RATE = 0.05
    MILL = 1000000
    print("""\nYear  Value (Million Dollars)
----  -----------------------""")
    
    for i in range(1, year + 1, 1):
        value = (principal * (1 + INTEREST_RATE) ** i) / MILL
        print("{: >4d}{: >25.6f}".format(i, value))
    return value

    
def perfect_square(num):
    """
    ------------------------------------------------------
    Prints all the perfect square numbers between 1 and
    num(exclusive)
    Its better to use a for loop so its easier to flow 
    through numbers between 1 and num (user input). 
    While doing that, we can use it to find the prime 
    numbers between that range by using an if statement
    within the for loop
    Use: split
    ------------------------------------------------------
    Parameters:
        num - User input (int)
    Returns:
        split - List of all Prime numbers upto num (int)
    ------------------------------------------------------
    """
    if(num < 0):
        print("\nYou did not enter a positive integer") 
    else:   
        split = (" ")
            
        for i in range(1, num):
            if ((math.sqrt(i) % 1) == 0):        
                split += str(i) + (", ")
        print("\nPerfect Squares below {} are: {}".format(num, split))
        return split

    
def factorial(num):
    """
    ------------------------------------------------------
    Uses a for loop to calculate and return 
    the factorial of num
    Use: value = factorial(num)
    ------------------------------------------------------
    Parameters:
        num - A number entered by user (int)
    Returns:
        value - Returns the factorial number for num(int)
    ------------------------------------------------------
    """    
    value = 1
    for i in range(1, num + 1, 1):
        value = value * i
    return value

    
def is_prime(num):
    """
    ------------------------------------------------------
    Determines whether the number is prime or not!
    A while loop was used to constantly keep asking 
    the user to input a positive integer if they had 
    entered zero or a number less than 0 
    Use: prime = is_prime(num)
    ------------------------------------------------------
    Parameters:
        num - A number entered by user (int)
    Returns:
        
    ------------------------------------------------------
    """  
    
    for i in range(2, num, 1):
        if(num % i == 0):
            return True    
        else:
            return False
    return True 
