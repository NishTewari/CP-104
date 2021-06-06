'''
-----------------------------------------------

-----------------------------------------------
Author: Nishant Tewari
ID: 190684430
Email: tewa4430@mylaurier.ca
__updated__ = "2019-10-12"
-----------------------------------------------

'''
# Imports

# Constants


def quadrant(x, y):
    """
    ------------------------------------------------------
    Determines which quadrant the coordinate 
    Use: quadrant = quadrant(x,y)
    ------------------------------------------------------
    Parameters:
        x - first number (int)
        y - second number (int)

    Returns:
        quadrant - returns which quadrant the coordinate 
        is in (String)
    ------------------------------------------------------
    """    
    if(x >= 0 and y >= 0):
        quadrant = "Q1"
    elif(x < 0 and y >= 0):
        quadrant = "Q2"
    elif(x <= 0 and y < 0):
        quadrant = "Q3"
    else:
        quadrant = "Q4"
        
    return quadrant
