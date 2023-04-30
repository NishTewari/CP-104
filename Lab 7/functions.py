'''
-----------------------------------------------
Functions for all Tasks in lab 7 
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2023-04-30"
-----------------------------------------------

'''
# Imports
from random import randint
# Constants


# Task 1 
def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """ 
    count = 0
    number = randint(1, high)
    
    while(high != number):
        high = int(input("Guess: "))
        count = count + 1
        if(high > number):
            print("Too high, try again.")
        elif(high < number): 
            print("Too low, try again")
        elif(high == number):
            print("Congratulations - good guess!")
    return count


# Task 2
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 0
    count = 0
    
    if(target == 0 or target == 1):
        power = 1
    else:
        while(target > power):
            count += 1
            power = 2 ** count
    
    return power
   
    
# Task 3
def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0 
    RATE_DEC = rate / 100
    while(target > current):
        current = current * (1 + RATE_DEC)
        years = years + 1
        
    return years


# Task 4
def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    

# Task 5
def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, net_pay, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, net_pay, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        net_pay - net_pay of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    num = float(input("First positive value: "))
    minimum = num
    maximum = num
    net_pay = num
    counter = 0
    n = 0
    while(num >= 0):
        num = float(input("Next positive value: "))
        counter += 1
        n += 1
        if num >= 0:
                net_pay = net_pay + num
                if num > maximum:
                    maximum = num
                elif num < minimum:
                    minimum = num
                    
    average = net_pay / n
    return minimum, maximum, net_pay, average


# Task 6
def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """ 
    positives = 0
    negatives = 0 
    zeroes = 0
    num = float(input("First value: "))
    
    if(num > 0):
        positives = 1
    elif(num < 0 and num != -999):
        negatives = 1
    elif(num == 0):
        zeroes = 1
    
    while(num != -999):
        num = float(input("Next value: "))
        
        if(num > 0):
            positives += 1
        elif(num < 0 and num != -999):
            negatives += 1
        elif(num == 0):
            zeroes += 1
            
    return negatives, zeroes, positives

        
# Task 7 
def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates net_pay costs for meals.
    Use: b_net_pay, l_net_pay, s_net_pay, a_net_pay = meal_costs()
    -------------------------------------------------------
    Returns:
        b_net_pay - net_pay breakfasts cost (float)
        l_net_pay - net_pay lunches cost (float)
        s_net_pay - net_pay suppers cost (float)
        a_net_pay - all meals cost (float)
    ------------------------------------------------------
    """
    n = 1 
    print("For Day 1\n")
    
    b_net_pay = float(input("How much was breakfast? $"))
    l_net_pay = float(input("How much was lunch? $"))
    s_net_pay = float(input("How much was supper? $"))
    
    away = input("\nWere you away another day (Y/N)? ")
    
    while (away == 'Y'):
        print("\nFor Day {}\n".format(n + 1))
    
        b_net_pay += float(input("How much was breakfast? $"))
        l_net_pay += float(input("How much was lunch? $"))
        s_net_pay += float(input("How much was supper? $"))
    
        away = input("\nWere you away another day (Y/N)? ")
        n += 1
    
    a_net_pay = b_net_pay + l_net_pay + s_net_pay
    return b_net_pay, l_net_pay, s_net_pay, a_net_pay


# Task 8 
def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expensess in a month. Calculate the
    net_pay expensess and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expensess, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (int >= 0)
    Returns:
        expensess - net_pay monthly expensess (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = 0
    user_value = float(input("Enter an expenses (0 to quit): $"))
    
    while(user_value != 0):
        expenses += user_value
        user_value = float(input("Enter another expenses (0 to quit): $"))
         
    balance = available - expenses
    if(balance == 0):
        status = "Balanced"
    elif(balance > 0):
        status = "Surplus"
    else:
        status = "Deficit"
    return expenses, balance, status


# Task 9 
def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input("Enter a value between 0 and high 100: "))
    if(value > high):
        print("Value entered is too high")
    elif(value < low):
        print("Value entered is too low")
       
    while(value > high or value < low):
        value = int(input("Enter a value between 0 and high 100: "))
        
        if(value > high):
            print("Value entered is too high")
        elif(value < low):
            print("Value entered is too low")
        
    return value
    
    
def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: net_pay, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        net_pay - net_pay net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    
    n = 0
    total = 0
    TAX_RATE = 0.03625
    OVERTIME_RATE = 1.5
    OVERTIME_HOUR = 40
    
    employee_id = int(input("Employee ID: "))

    while (employee_id > 0):
        hourly_rate = int(input("Hourly wage rate: "))
        hours_worked = int(input("Hours worked: "))
           
        if(hours_worked > OVERTIME_HOUR):
            net_pay = (hourly_rate * OVERTIME_HOUR) + ((hours_worked - OVERTIME_HOUR) * hourly_rate * OVERTIME_RATE)
            net_pay = net_pay - (net_pay * TAX_RATE)
            total += net_pay
        else:
            net_pay = hourly_rate * hours_worked 
            net_pay = net_pay - (net_pay * TAX_RATE)
            total += net_pay
            
        print("Net payment for employee {}: ${:,.2f}".format(employee_id, net_pay))
        employee_id = int(input("\nEnter next employee ID: "))
        
        n += 1
        
    average = total / n
       
    return total, average
