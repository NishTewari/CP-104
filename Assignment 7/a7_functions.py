'''
-----------------------------------------------
Assignment Seven Functions 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-08"
-----------------------------------------------
'''
def win_game():
    """
    ------------------------------------------------------
    Checks how many times the strings "red" and "green" are 
    used by the user and returned as a list
    I used a while loop so it would be easier to print the 
    multiple user input statements until the while loop comes
    to an end. This allows the while to run forever until 
    the condition is met.  
    Use: counter_list = win_game() 
    ------------------------------------------------------
    Parameters:
        None
    Returns:
        counter_list- list of both the number of times each
        string is used(int)
    ------------------------------------------------------
    """ 
    counter_list = [0, 0]
    empty_string = "" 
    
    user_value = input('Enter "red" or "green" or press ENTER to stop: ')
    
    if(user_value.lower() == "red"):
        counter_list[0] += 1
    elif(user_value.lower() == "green"):
        counter_list[1] += 1
       
    while (user_value != empty_string):
        
        user_value = input('Enter "red" or "green" or press ENTER to stop: ')   
        
        if(user_value.lower() == "red"):
            counter_list[0] += 1
        elif(user_value.lower() == "green"):
            counter_list[1] += 1
            
    return counter_list


def display_pattern(num_lines):
    """
    ------------------------------------------------------
    Prints a right triangle 
    Use: display_pattern(num_lines)
    ------------------------------------------------------
    Parameters:
        num_lines - the number of lines of that
        will determine the size of the triangle (int)
    Returns: 
        None
    ------------------------------------------------------
    """  
    for row in range(num_lines):
        for col in range(num_lines):
            if col == 0 or row == (num_lines - 1) or row == col:
                print("#", end="")
            else:
                print(end=" ")
        print()
    return None


def keep_positive_numbers():
    """
    ------------------------------------------------------
    Keep asking the user to enter positive numbers until 
    a zero is entered. This will create a list of numbers 
    Use: positive_list = keep_positive_numbers()
    ------------------------------------------------------
    Parameters:
    Returns:
        positive_list - returns a list of all 
        positive integers (int > 0)
    ------------------------------------------------------
    """ 
    num = None
    positive_list = []
    
    while not num == "0":
        
        num = input("Enter a positive integer: ")
        
        if(num.isdigit() and num != "0"):
            positive_list.append(int(num))
            
    return positive_list


def find_value(num_list, target):
    """
    ------------------------------------------------------
    Find the index location of the target in a positive
    integer list. 
    Use: target_location = find_value(num_list, target)
    ------------------------------------------------------
    Parameters:
        num_list - list of positive integers (int > 0)
        target -  a number where the user is asking 
        the program to find in the list (int)
    Returns:
        target_location - Returns the index location(s)
        of where the target is in the list (int)
    ------------------------------------------------------
    """  
    index = 0
    target_location = []   
    for i in range(len(num_list)):
        if(target == num_list[i]):
            target_location.append(index)
        index += 1
                
    return target_location
       
