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
BASE_PRICE_RATE = 0.08

DISCOUNT_EVENING = 0.25
DISCOUNT_MIDNIGHT = 0.50

OVER_LENGTH = 30
DISCOUNT_OVER_LENGTH = 0.10 


def base_price(length):
    """
    ------------------------------------------------------
    Determines the base price of the call 
    Use: price = base_price(length)
    ------------------------------------------------------
    Parameters:
        length - time in minutes (int)
    Returns:
        price - the price of the call (float)
    ------------------------------------------------------
    """  
    price = length * BASE_PRICE_RATE
    
    return price 

    
def time_discount(price, hour):
    """
    ------------------------------------------------------
    Determines the discount the user will receive depending
    on what time the call is made 
    Use: price = time_discount(price,hour)
    ------------------------------------------------------
    Parameters:
        price - price of the call (float)
        hour - the time it is currently (int)
    Returns:
        price - the price of the call (float)
    ------------------------------------------------------
    """
    hour = hour % 24
    if(hour >= 18 and  hour <= 23):
        price = price * (1 - DISCOUNT_EVENING)
    elif(hour >= 0 and hour < 8):
        price = price * (1 - DISCOUNT_MIDNIGHT)

    return price    


def length_discount(price, length):
    """
    ------------------------------------------------------
    Determines the discount the user will receive depending
    on how long the call is 
    Use: price = length_discount(price,length)
    ------------------------------------------------------
    Parameters:
        price - the price of the call (float)
        length - the length of the call in minutes (int)

    Returns:
        price - the price of the call(float)
    ------------------------------------------------------
    """
    # If the call happens to be more than 30 mins than apply a discount. 
    if(length > OVER_LENGTH):
        price = price * (1 - DISCOUNT_OVER_LENGTH)
    return price
