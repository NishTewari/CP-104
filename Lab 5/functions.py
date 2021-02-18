'''
-----------------------------------------------
Functions for all Tasks in lab 5 
-----------------------------------------------
Author: Nish Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2021-02-16"
-----------------------------------------------

'''
#Constants


#Function for t01
def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    #checking if day*month is the same value as year.
    if day*month == year: 
        magic = True   #since the condition is true
    else:
        magic = False 
    return magic


#Function for t02
def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg) × acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    #Constant
    ACCELRATION = 9.8

    #Calculate the weight of object in Newtons
    weight = mass * ACCELRATION

    if weight >= 1000:
        message = "heavy"
    elif weight <= 10:
        message = "light"
    else:
        message = "average"  

    return message 

#Function for t03 
def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """
    #Constants for the gym discount percentage % 
    DISCOUNT_ONE = 5 # 5% discount for 1 friend
    DISCOUNT_TWO = 10 # 10% discount for 2 friends
    DISCOUNT_PLUS = 15 # 15% discount for 3+ friends

    if friends == 0: #if 0 friends :( final cost will be the same as the cost parameter  
        final_cost = cost
    elif friends == 1: # if 1 friend, 5% of cost parameter will be deducted 
        final_cost = cost - (cost*(DISCOUNT_ONE/100))
    elif friends == 2:
        final_cost = cost - (cost*(DISCOUNT_TWO/100))
    else:
        final_cost = cost - (cost*(DISCOUNT_PLUS /100))
    return final_cost


#Function for t04
def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    #We use abs which is absolute value, this is due to possibly having a value that may be less than the target (v1 > target)
    #Calculate the distance between target and the first value 
    first_distance = abs(target - v1)
    #Calculate the distance between target and the second value 
    second_distance = abs(target - v2)

    #check condition if the first distance between target and v1 is greater than target and v2 
    if first_distance >  second_distance:
        result = v2     #if the statement above is true, we will set result as v2 since target/v2 is a shorter distance 
    else:
        result = v1
    return result

#Function for t05
def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    
    result = False
    if(year % 4 == 0 and year % 100 != 0):
        result = True
    elif(year % 100 == 0 and year % 400 == 0):
        result = True
    else: 
        result = False
    return result

#Function for t06
def is_divisible(n, i, j):
    """
    -------------------------------------------------------
    Determines if n is evenly divisible by both i and j.
    Use: result = is_divisible(n, i, j)
    -------------------------------------------------------
    Parameters:
        n - the number to check for divisibility (int)
        i - one of the values to divide n by (int)
        j - another value to divide n by (int)
    Returns:
        result - True if n is evenly divisible by both
            i and j, False otherwise (boolean)
    ------------------------------------------------------
    """
    