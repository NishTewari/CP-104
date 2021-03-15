'''
-----------------------------------------------
Question Two Functions
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-15"
-----------------------------------------------

'''
# Imports
import random

def math_quiz():
    """
    ------------------------------------------------------
    Generates two integers to solve a math question 
    Use: math_quiz()
    ------------------------------------------------------
    Parameters:
        
    Returns:
        
    ------------------------------------------------------
    """    
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    
    print("  {:>3d}".format(num1))
    print("+ {:>3d}".format(num2))
    print()
    answer = int(input("Answer: "))
    print()
    
    if(answer != (num1 + num2)):
        print("Incorrect - the answer should be: {}".format(num1 + num2))
    else: 
        print("Congratulations, correct answer!")
    
