'''
-----------------------------------------------
Lab Ten Functions 
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-11-19"
-----------------------------------------------

'''
# Imports

# Constants


# Task 1
def customer_record(fv, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fv, n)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """

    fv.seek(0)
    result = []
    line = fv.readline()
    counter = 0
    
    while line != "" and counter != n: 
        line = fv.readline()
        counter += 1    
    if line != "" :
        line = line.strip()
        result = line.split(',')
    
    return result


# Task 6 
def number_stats(fv):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    fv.seek(0)
    smallest = int(fv.readline())
    largest = smallest
    total = 0
    number = 0 
    counter = 0  
    fv.seek(0)
    
    for number in fv:
        if int(number) < smallest:
            smallest = int(number)
        elif int(number) > largest:
            largest = int(number)
        counter += 1
        total += int(number) 
    average = total / counter
            
    return smallest, largest, total, average 
    
    
# Task 10     
def count_frequency_word(fv, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fv.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fv, word)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        word - the word to search for it in fv (str)
    Returns:
        count - the number of appearance of word in fv (int)
    ------------------------------------------------------
    """
    
    fv.seek(0)
    count = 0
    
    for line in fv:
        if line.strip() == word:
            count += 1  
    return count 

    
# Task 12    
def find_shortest(fv):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fv.
    Assumes file is not empty.
    Use: word = find_shortest(fv)
    -------------------------------------------------------
    Parameters: 
        fv - file to search (file - open for reading)
    Returns:
        word - the first word with the shortest length in fv (str)
    ------------------------------------------------------
    """
    fv.seek(0)
    word = fv.readline()
    fv.seek(0)
    
    for line in fv:
        line = line.strip()
        line = line.split(" ")
        for i in range(len(line)):
            if(len(line[i]) < len(word)):
                word = line[i]
    return word 


# Task 14 
def file_copy_n(fv_1, fv_2, n):
    """
    -------------------------------------------------------
    Copies n record from fv_1 (starting from the beginning of the file) to fv2
    Use: file_copy_n(fv_1, fv_2, n)
    -------------------------------------------------------
    Parameters:
        fv_1 - file to search (file - open for reading)
        fv_2 - file to search (file - open for appending)
    Returns:
        None
    ------------------------------------------------------
    """
    fv_1.seek(0)
    fv_2.seek(0)
    counter = 0 
    line = fv_1.readline()
    
    while line != "" and counter != n:
        fv_2.write(line)
        line = fv_1.readline()
        counter += 1
        
    return None
    
