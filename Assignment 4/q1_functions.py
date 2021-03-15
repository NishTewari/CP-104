'''
-----------------------------------------------
Question one Functions 
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-15"
-----------------------------------------------
'''

def calc_federal_tax(income):
    """
    ------------------------------------------------------
    Calculates the federal tax 
    Use: federal_tax_total = calc_federal_tax(income)
    ------------------------------------------------------
    Parameters:
        income - The income the user enters (int)
    Returns:
        federal_tax_total - Federal tax amount (int)
    ------------------------------------------------------
    """   
    #constants  
    BELOW_TAX = 0.15
    BETWEEN_TAX = 0.25
    OVER_TAX = 0.35 
    
    first_income = (35000) * (BELOW_TAX)
    second_income = (99999 - 35001) * (BETWEEN_TAX)
    third_income = (income - 100000) * (OVER_TAX)
    
    federal_tax_total = first_income + second_income + third_income
    return(federal_tax_total)
    
    
def calc_prov_tax(income):
    """
    ------------------------------------------------------
    Calculates the provincial tax 
    Use: state_income_tax = calc_prov_tax(income)
    ------------------------------------------------------
    Parameters:
        income - The income the user enters (int)
    Returns:
        state_income_tax - Provincial tax amount (int) 
    ------------------------------------------------------
    """    
    FLAT_RATE = 0.05
   
    state_income_tax = (income - 50000) * FLAT_RATE
    return(state_income_tax)
