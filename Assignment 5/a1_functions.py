'''
-----------------------------------------------
Assignment Five, Question One Functions
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-15"
-----------------------------------------------

'''
def max_three(x, y, z):
    """
    ------------------------------------------------------
    Determine the average of the two smaller values 
    Use: average = max_three(x,y,z)
    ------------------------------------------------------
    Parameters:
        x - first number (float)
        y - second number (float)
        z - third number  (float)
    Returns:
        average - the average of the two smaller values (float)
    ------------------------------------------------------
    """    
    if(x < y and z < y):
        average = (x + z) / 2
        
    elif(x < z and y < z):
        average = (x + y) / 2
    else:
        average = (z + y) / 2

    return average
