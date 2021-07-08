'''
-----------------------------------------------
Assignment Eight Functions  
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-08"
-----------------------------------------------
'''
#Question One
def sum_digit_string(my_str):
    """
    ------------------------------------------------------
    Sums all the digits in my_str, ignores non-digit
    characters
    Use: total = sum_digit_string (my_str)
    ------------------------------------------------------
    Parameters:
        my_str: - string that has single-digit numbers (str)
    Returns:
        total: sum of all the single digit number (integer >= 0)
    ------------------------------------------------------
    """  
    total = 0 
    for num in str(my_str)[0:]:
        if num.isdigit() and int(num) in range(10):
            total += int(num)
        
    return total 


#Question Two 
def find_frequent(my_str):
    """
    ------------------------------------------------------
    Finds the most frequent character in a string 
    Use: char = find_frequent(my_str)
    ------------------------------------------------------
    Parameters:
        my_str: - string entered by user (str)
    Returns:
        char:  returns the character that is most used
        in the string(string)
    ------------------------------------------------------
    """   
    string = ""
    
    if my_str is not string:
        count = 0
        char = my_str[0]
        for letter in my_str:
            frequent_char = my_str.count(letter)
            if(frequent_char > count):
                count = frequent_char
                char = letter
    else:
        char = None 
    return char 


#Question Three
def string_capitalizer(my_str):
    """
    ------------------------------------------------------
    Capitalizes the first letter of each word at the 
    beginning of a sentence after a "." or "?"
    Use: correct_string = string_capitalizer(my_str)
    ------------------------------------------------------
    Parameters:
        my_str: - user input string (str)
    Returns:
        correct_string: returns the new string(string)
    ------------------------------------------------------
    """ 
    correct_string = None
    
    if (my_str != ""):
        temp_list = []
        temp1 = 0 
        for i in range(0, len(my_str)):
            if(my_str[i] == "?" or my_str[i] == "."):
                temp_list.append(my_str[temp1: i + 1])
                temp1 = i + 2
                
        my_str = ""
        for i in temp_list:
            i = list(i)
            i[0] = i[0].upper()
            i = ''.join(i)
            my_str += i
            my_str += " "
        correct_string = my_str
    return correct_string

#Question Four
def is_word_chain(my_list):
    """
    ------------------------------------------------------
    Checks if the list is a word chain or not? 
    Use: check_chain = is_word_chain(my_list)
    ------------------------------------------------------
    Parameters:
        my_list - A list of names (list)
    Returns:
        check_chain - boolean return(bool)
    ------------------------------------------------------
    """   
    if(len(my_list) <= 1):
        check_chain = False
    else:
        check_chain = True
        counter = 0
        while(check_chain == True and counter < len(my_list) - 1):
            if my_list[counter][-1].lower() != my_list[counter + 1][0].lower():
                check_chain = False
            counter += 1
    return check_chain
        
