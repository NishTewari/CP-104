'''
-----------------------------------------------
Functions for all Tasks in lab 5 
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-06-06"
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
    #if the remainder between n/i & n/j is 0. This means that they are evenly divisble 
    if n % i == 0 and n % j == 0:
        result = True
    else:
        result = False
    return result

#Function for t07
def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """
    #Constants
    TAX_RATE = 0.03625
    EXTRA_PAY = 1.5
    FORTY = 40

    #Checking if the employee has worked over forty hours 
    if hours_worked > FORTY: 
        #example: 20$hour, 45 hours 
        #(20 * 40) + ((45 - 40)*1.5*20) --> hence the 5 extra hours will be the only hours receving the extra bonus :) 
        total_before_tax = (hourly_rate * FORTY) + ((hours_worked - FORTY)*(EXTRA_PAY * hourly_rate))
        net_payment = total_before_tax - (total_before_tax * TAX_RATE) # apply tax :(
    else:
        total_before_tax = (hours_worked * hourly_rate)  #Simply multiply the hours they worked by their hourly rate
        net_payment = total_before_tax - (total_before_tax * TAX_RATE) # apply tax :(
    return net_payment

#Function for t08 
def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n 
        is not between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    #setting a condition so that numbers 1-10 convert to Roman Numerals  
    if(n == 1):
        numeral = "I"
    elif(n == 2):
        numeral = "II"
    elif(n == 3):
        numeral = "III"
    elif(n == 4):
        numeral = "IV"
    elif(n == 5):
        numeral = "V"
    elif(n == 6):
        numeral = "VI"
    elif(n == 7): 
        numeral = "VII"
    elif(n == 8): 
        numeral = "VIII"
    elif(n == 9): 
        numeral = "IX"
    elif(n == 10):
        numeral = "X"
    else: 
        numeral = None
    return numeral

#Function for t09
def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if speed < 39:
        category = "Breeze"
    elif speed >= 39 and speed <= 61:
        category = "Strong Wind"
    elif speed >= 62 and speed <= 88:
        category = "Gale Winds "
    elif speed >= 89 and speed <= 117:
        category = "Whole Gale"
    elif speed > 117:
        category = " Hurricane"
    return category

#Function for t10
def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    if(intensity < 5):
        result = "Little or no damage"
    elif(intensity >= 5 and intensity < 5.5):
        result = "Some damage"
    elif(intensity >= 5.5 and intensity < 6.5):
        result = "Serious damage: Walls may crack or fall"
    elif(intensity >= 6.5 and intensity < 7.5):
        result = "Disaster: houses and buildings may collapse"
    else:
        result = " Catastrophe: most buildings destroyed"
    return (result)

#Function for t11   
def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - name of: quadrant, axis, or origin of 
        coordinate x, y (str)
    -------------------------------------------------------
    """
    if x > 0 and y > 0:
        location = 'Quadrant 1'
    elif x < 0 and y > 0:
        location = 'Quadrant 2'
    elif x < 0 and y < 0:
        location = 'Quadrant 3'
    elif x > 0 and y < 0:
        location = 'Quadrant 4' 
    elif x == 0 and y == 0:
        location = 'Origin'
    elif x == 0:
        location = 'Y-Axis'
    else:
        location = 'X-Axis'
    return location

#Functions for t12
def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time >= 10 years service
        1.5% for full time < 4 years service
        3% for part time > 10 years service
        1% for part time < 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    #Constants --> Salary raise percentage.
    FULL_TEN = 5
    FULL_FOUR = 1.5
    PART_TEN_PLUS = 3
    PART_FOUR = 1
    OTHER = 2 

    if status == 'F' and years >= 10:
        new_salary = salary + (salary * (FULL_TEN/100))   #5% raise 
    elif status == 'F' and years < 4:   
        new_salary = salary + (salary * (FULL_FOUR/100))   #1.5% raise
    elif status == 'P' and years > 10:
        new_salary = salary + (salary * (PART_TEN_PLUS/100)) #3% raise
    elif status == 'P' and years < 4:
        new_salary = salary + (salary * (PART_FOUR/100))  #1% raise 
    else: 
        new_salary = salary + (salary * (OTHER/100))  #2% raise
    return new_salary

#Function for t13
def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    year = int(input("Years Employed: "))
    ann_sal = int(input("Annual Salary: "))

    if year >= 5 and ann_sal >= 30000:
        qualified = True
    else: 
        qualified = False 
    return qualified

#Function for t14
def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    INFANT = 3
    SENIOR = 65

    age = int(input("How old are you? "))

    if age < INFANT: 
        price = 0
    elif age >= SENIOR: 
        price = 4
    elif age >= 10 and age < 18:
        student = (input("Are you a student at this school? (Y/N): "))
        if student == "Y":
            price = 1
        else: 
            price = 3
    elif age >= 18 and age < 65:
        price = 5
    else: 
        price = 2 
    
    return price 


#Function for t15
def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER = 6
    WINGS = 8
    FRIES = 1.5
    SALAD = 2
    
    price = 0
    
    order_b = input("Order B - burger or W - wings: ")
    combo = input("Make it a combo? (Y/N): ")
    
    if(order_b == 'B'):
        price = BURGER
    else: 
        price = WINGS
    if(combo == 'Y'):
        add = input("Add  F - fries or S - salad: ")
        if(add == 'F'):
            price = price + FRIES
        if(add == 'S'):
            price = price + SALAD
       
    return price
    

