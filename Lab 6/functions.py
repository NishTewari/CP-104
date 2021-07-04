'''
-----------------------------------------------
Lab Six, Functions 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
#Task 1
def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0 
    #for i in range(starting Val, ending Val, increment by)
    for i in range(2, num + 1, 2):
        if(i % 2 == 0):
            total += i

    return total 

#Task 2
def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0 

    #for i in range(starting Val, ending Val, increment by)
    for i in range(1, num + 1, 2):
        if(i % 2 != 0): 
            total += i  #Adding i; since i is all the odd #s within given list of numbers 

    return total 

#Task 3
def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """

    total = 0 

    for i in range (start, finish + 1, increment):
        total += i 
    return total

#Task 4 
def sum_partial_harmonic(n):
    """
    -------------------------------------------------------
    Sums and returns the total of a partial harmonic series.
    This series is the sum of all terms 1/i, where i ranges
    from 1 to n (inclusive)
    i.e. 1 + 1/2 + 1/3 + ... + 1/n
    Use: total = sum_partial_harmonic(n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int > 0)
    Returns:
        total - sum of partial harmonic series from 1 to n (int)
    ------------------------------------------------------
    """
    total = 0 

    for i in range(1, n+ 1):
        total += (1/i)
    return total 

#Task 5 
def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range (height):
        print(char * width)
    return None

#Task 6
def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    #?????
    k = (2 * height) - 2
    for p in range(height):
        for n in range(k):
            print(end=" ")
        k = k - 1
        for n in range(0, p + 1):
            print(char, end=' ')
        print(" ")
    return None 

#Task 7 
def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
#Task 8
def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

#Task 9 
def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(n, 1, -1):
        print('''{} bottles of beer on the wall, {} bottles of beer.
Take one down, pass it around, {} bottles of beer on the wall.\n'''.format(i,i,i-1))
       
    print('''{} bottle of beer on the wall, {} bottle of beer.
Take one down, pass it around, no more bottles of beer on the wall!'''.format(i,i))
    
    return None 

# Task 10 
def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(start, end + 1 , inc):
        print("Calories burned after {} minutes: {:.1f}".format(i, i*burnt_per_minute))

#Task 11
def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print("Age \t Salary")
    print("-----------------")
    
    
    for i in range(age, 66, 1):
        print("{} \t {:,.2f}".format(i, salary))
        salary = salary + (salary * (increase/100))

#Task 12       
def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print("Year \t Value $")
    print("-----------------")

    final_value = value 

    for i in range (0, years + 1, 1):
        print("{} \t {:,.2f}".format(i, final_value))
        final_value = final_value * (1 + (rate/100))
    return final_value 

#Task 13
def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    print('Base\tHeight\tCross_Sectional Area\tMoment of Inertia\tSection Modulus')    
    for i in range(b_min, b_max + 1, b_inc):
        for j in range(h_min, h_max + 1, h_inc): 
            cross_SectArea  =  (i * j) 
            mom_Inertia = ((i * (j**3)) / 12)
            section_Mod = ((i * (j**2)) / 6)
            #print("%d\tx\t\t%d\t\t\t%.2f\t\t\t\t%.2f\t\t\t\t%.2f" % (i, j, cross_SectArea, mom_Inertia, section_Mod))
    return None 

#Task 14 
def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    total_hours = 0 
    for i in range(1, 7, 1):
        print("\nWeek {}".format(i))
        for j in range(1, ia_count + 1, 1):
            hours = float(input("Marking hours for IA {}:".format(j)))
            total_hours += hours
    return total_hours

#Task 15
def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    first = float(input("First Value: "))
    total = first 
    for i in range(1, n, 1):
        next_val = float(input(("Next value: ")))
        total += next_val

        if(i == 1):
            minimum = first 
            maximum = first 
        
        if(next_val < minimum):
            minimum = next_val 
        elif(next_val > maximum):
            maximum = next_val
    average = total / n
    return minimum, maximum, total, average 