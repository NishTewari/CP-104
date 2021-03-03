'''
-----------------------------------------------
Assignment Three, Question Four
-----------------------------------------------
Author: Nish Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-03-02"
-----------------------------------------------
'''
#Constants
FAT_CALO_MULTIPLIER = 9
CARB_CALO_MULTIPLIER = 4


def calculate_calories(fat_gram, carbs_gram):
    """
    ------------------------------------------------------
    Calculates the amount of calories from fat and carbs
    Use: fat_calories = fat_gram * 9 and carb_calories = carbs_gram * 4  
    ------------------------------------------------------
    Parameters:
        fat_gram - amount of grams in fat
        carbs_gram - amount of grams in carbs 
    Returns:
        fat_calories - amount of calories from fat 
        carb_calories - amount of calories from carb
    ------------------------------------------------------
    """    
    fat_calories = fat_gram * FAT_CALO_MULTIPLIER
    carb_calories = carbs_gram * CARB_CALO_MULTIPLIER
    return(fat_calories, carb_calories)


def main():
    #User input 
    fat_gram   = int(input("Enter the fat grams consumed: "))
    carbs_gram = int(input("Enter the carbohydrate grams consumed: "))
    
    #Calling the function
    fat_calories, carb_calories = calculate_calories(fat_gram, carbs_gram)
    
    
    print("\nTotal calories a total of {} [Fat calories: {:.2f} and Carb calories: {:.2f}]".format(fat_calories + carb_calories, fat_calories, carb_calories))

    
main()

