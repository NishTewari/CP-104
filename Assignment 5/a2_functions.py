'''
-----------------------------------------------
Assignment Five, Question Two Functions
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-15"
-----------------------------------------------
'''
def pocket_color(num):
    """
    ------------------------------------------------------
    Displays the according pocket color depending on the pocket number
    Use: color = pocket_color(num)
    ------------------------------------------------------
    Parameters:
        num - a pocker number (int)
    Returns:
        color - a pocket color (String)
    ------------------------------------------------------
    """    
    # Pocket 0
    if(num == 0):
        color = "green"
        
    # Pockets 1 through 10     
    elif(num >= 1 and num <= 10):
        if(num % 2 == 0):
            color = "black"
        else:
            color = "red"
            
    # Pockets 11 through 18         
    elif(num >= 11 and num <= 18):
        if(num % 2 == 0):
            color = "red"
        else:
            color = "black" 
             
    # Pockets 19 through 28          
    elif(num >= 19 and num <= 28):
        if(num % 2 == 0):
            color = "black"
        else:
            color = "red" 
            
    # Pockets 29 through 36          
    elif(num >= 29 and num <= 36):
        if(num % 2 == 0):
            color = "red"
        else:
            color = "black" 
    else: 
        color = "ERROR"   
    return color
     
