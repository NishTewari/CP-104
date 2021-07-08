'''
-----------------------------------------------
Lab Eight, Task 1
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-03"
-----------------------------------------------
'''
from random import randint
#Task 1
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    DOW = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    for i in range(0,d):
        name = DOW[i]
    return name

#Task 2
def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for i in range(0, m):
        name = month_names[i]
        
    return name

#Task 3
def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    digit_number = [1,2,3,4,5,6,7,8,9]

    for i in range(0,n):
        name = digit_number[i]
    
    return name

#Task 4
def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    #this line basically does everything in one step
    #make a list using randint for the number of values in range! 
    values = [randint(low,high) for i in range(0,n)]

    return values

#Task 5
def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    numbers = []
    
    for i in range(n):
        num = randint(low, high)
        
        while num in numbers:
            num = randint(low, high)
        numbers.append(num)
    return numbers

#Task 6 
def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    total = 0 
    sorted_array = []
    for ele in range(0, len(values)):
        total = total + values[ele]

    while values:
        min = values[0]
        for x in values:
            if x < min:
                min = x
        sorted_array.append(min)
        values.remove(min)
    smallest = sorted_array[0]
    largest = sorted_array[-1]
    average = total / len(sorted_array)

    return smallest, largest, total, average 
    
#Task 7     
def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = 0
    positives = 0
    zeroes    = 0 
    evens     = 0 
    odds      = 0 
    for ele in values:
        if ele <= -1: 
            negatives += 1
        elif ele  >= 1:
            positives += 1
        elif ele  == 0: 
            zeroes += 1
        if (ele % 2) == 0:
            evens += 1 
        else:
            odds += 1
    return negatives,positives,zeroes,evens,odds

#Task 8 
def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    Use: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """
    index = -1
    counter = 0
   
    while counter < len(a) and index == -1:
        
        if(a[counter] == v):
            index = counter

        counter += 1
      
    return index
    
        
#Task 9    
def many_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns a list of
    all indexes of its occurrence.
    Use: indexes = many_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        indexes - a list of indexes of the location of v in a,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    index_counter = 0
    indexes = [] 

    for elements in a: 
        if v == elements:
            indexes.append(index_counter)          
        index_counter+=1 

    return indexes

#Task 10
def min_search(a):
    """
    -------------------------------------------------------
    Searches through a for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes a has at least
    one element.)
    Use: indexes = min_search(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
    Returns:
        indexes - a list of indexes of the minimum values in
            a (list of int).
    -------------------------------------------------------
    """
   
    indexes = []
    counter = 0 
    for elements in a: 
        if min(a) == elements:
            indexes.append(counter)
        counter += 1
    
    return indexes 

#Task 11          
def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: target = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - source1 ⋅ source2 [source1 dot product source2] (float)
    -------------------------------------------------------
    """
    target = 0

    for i in range(0,len(source1),1):
        target = target + source1[i] * source2[i]
       

    return target

#Task 12
def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sum(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []

    for i in range(0,len(source1),1):
        target.append(source1[i] + source2[i])
    return target

#Task 13
def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the union of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = [] 
    temp = [] 

    temp = source1 + source2

    for num in temp: 
        if num not in target:
            target.append(num)
    return target    

#Task 14
def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the intersection of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    temp_list = [elements for elements in source1 if elements in source2]

    for i in temp_list:
        if i not in target:
            target.append(i)
    return target

#Task 15 
def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    