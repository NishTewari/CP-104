'''
-----------------------------------------------
Assignment 9 Functions 
-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-11-23"
-----------------------------------------------

'''
# Imports

# Constants


# Question 1
def sum_numbers(fv):
    """
    ------------------------------------------------------
    Finds the digits within a sentence and returns the 
    total sum 
    Use: list, sum_digits = sum_numbers(fv)
    ------------------------------------------------------
    Parameters:
        fv - file to search for  (file)
    Returns:
        lst - list of the equation(list)
        sum_digits - total sum of digits
    ------------------------------------------------------
    """
    
    line = fv.readline() 
    lst = []
    sum_digits = 0
    
    for words in line.split():
        if words.isdigit():
            lst.append(int(words)) 
    for count in lst:
        sum_digits += count 
    return lst, sum_digits
       
    
# Question 2
def find_median(fv):
    """
    ------------------------------------------------------
    Finds the median Number for a list of numbers found in
    numbers file 
    Use: list, median = find_median(fv)
    ------------------------------------------------------
    Parameters:
        fv - file to search for (file)
    Returns:
        lst - lst of the numbers found in the file(list)
        median - the median within the numbers
    ------------------------------------------------------
    """
    lst = []
    line = fv.readline()
    count = 0 
    while line != "":
        for i in line.split():
            lst.append(int(i))
            count += 1
        line = fv.readline()
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        median = (lst[(length) // 2] + lst[(length) // 2 - 1]) // 2 
    else:
        median = lst[(length - 1) // 2]
        
    return lst, median 


# Question 3 
def analysis_file(file_in):
    """
    ------------------------------------------------------
    Finds the number of upper case and lower case letters,
    the number of digits and white space
    Use: upper_case, lower_case, digit_count, white_space 
    = analysis_file(file_in)
    ------------------------------------------------------
    Parameters:
        file_in - file to search for (file)
    Returns:
        upper_case - number of upper case letters (int)
        lower_case - number of lower case letters (int)
        digit_count - number of digits (int)
        white_space - number of white space(int)
    ------------------------------------------------------
    """
    line = file_in.readline()
    upper_case = 0 
    lower_case = 0
    digit_count = 0
    white_space = 0 
    
    while line != "":
        
        for i in line:
            if i.isupper():
                upper_case += 1
            elif i.islower():
                lower_case += 1
            elif i.isdigit():
                digit_count += 1
            elif i.isspace():                
                white_space += 1
            
        line = file_in.readline()
     
    return upper_case, lower_case, digit_count, white_space


# Question 4 
def valid_sn(txt_srl):
    """
    ------------------------------------------------------
    Checks if a serial number is valid or not 
    Use: result = valid_sn(txt_srl)
    ------------------------------------------------------
    Parameters:
        txt_srl - Serial number text
    Returns:
        result - Returns true or false (Bool)
    ------------------------------------------------------
    """
    result = True
    serial_str = txt_srl.strip()
    if len(serial_str) != 11:
        result = False 
    elif serial_str[:3] != 'SN/' or serial_str[3:7].isdigit() == False or serial_str[7:8] != '-' or serial_str[8:].isdigit() == False:
        result = False
    return result


# Question 4
def valid_sn_file(fv, new_file_1, new_file_2):
    """
    ------------------------------------------------------
    Distributes the serial numbers within two files.
    Use: valid_sn_file(fv, new_file_1, new_file_2)
    ------------------------------------------------------
    Parameters:
        fv - file to search for (file)
        new_file_1 - new file for valid inputs
        new_file_2 - new file for invalid inputs
    Returns:
        None 
    ------------------------------------------------------
    """
    txt_srl = fv.readline()
    while txt_srl != '':
        valid_check = valid_sn(txt_srl)
        if valid_check == True:
            new_file_1.write(txt_srl)
        else:
            new_file_2.write(txt_srl)
        txt_srl = fv.readline()
    return None
    
