'''
-----------------------------------------------
Question Three Functions
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-15"
-----------------------------------------------

'''

def num_day(day_num):
    """
    ------------------------------------------------------
    Prints the day of the week according to its day number 
    Use: day_week = num_day(day_num)
    ------------------------------------------------------
    Parameters:
        day_num - Number of the day (Int)
    Returns:
        day_week - Day of the week (String)
    ------------------------------------------------------
    """    
    if(day_num == 1):
        day_week = "The number 1 corresponds to Monday."
    elif(day_num == 2):
        day_week = "The number 2 corresponds to Tuesday."
    elif(day_num == 3):
        day_week = "The number 3 corresponds to Wednesday."
    elif(day_num == 4):
        day_week = "The number 4 corresponds to Thursday."
    elif(day_num == 5):
        day_week = "The number 5 corresponds to Friday."
    elif(day_num == 6):
        day_week = "The number 6 corresponds to Saturday."
    elif(day_num == 7): 
        day_week = "The number 7 corresponds to Sunday."
    else:
        day_week = "Sorry, that is not a valid number."    
    return(day_week)
        
