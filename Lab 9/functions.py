'''
-----------------------------------------------
Lab Nine, Functions
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
#Task 1
def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    hydroxide = False 
    if chemical[-2::1] == 'OH':
        hydroxide = True 
        return hydroxide  

#Task 2    
def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    if url[-3:] == "com":
        url_type = 'Business'
    elif url[-3:] == "org":
        url_type = 'non-profit'
    else: 
        url_type = 'Other'
    return url_type

#Task 3
def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    for characters in product_code:
        pc = product_code[0:3]
        pi = product_code[3:7]
        pq = product_code[7:]
    return pc,pi,pq

#Task 4
def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    
    return None

#Task 5
def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """

    return None 

#Task 6
def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    if(s.lower() == s.lower()[::-1]):
        palindrome = True
    else: 
        palindrome = False 
    return palindrome 

#Task 7 
def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0 
    
    for i in s: 
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            count += 1
    return count 

#Task 8 
def digit_count(s):
    """
    -------------------------------------------------------
    Counts the number of digits in a string.
    Use: count = digit_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of digits in s (int)
    -------------------------------------------------------
    """
    count = 0 
    
    for i in s: 
        if(i.isdigit()):
            count += 1
    return count

# Task 9   
def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    count = 0 
    
    for i in s: 
        if(i == '#' or i == '@' or i == '$' or i == '%' or i == '&' or i == '!'):
            count += 1
    return count 

#Task 10 
def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr   = 0 
    lowr   = 0 
    dgts   = 0
    whtspc = 0
    for characters in txt:
        if characters.isupper() == True:
            uppr += 1 
        elif characters.islower() == True:
            lowr += 1
        elif characters.isdigit() == True:
            dgts += 1
        elif characters == ' ': 
            whtspc += 1

    return uppr, lowr, dgts, whtspc

#Task 11
def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with its vowels removed (str)
    -------------------------------------------------------
    """
    vowels = "aeiouAEIOU"

    out = " "

    for characters in s:
        if characters in vowels:
            out = s.replace(characters, "")
    return out 

#Task 12
def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    comma = ","
    out = s

    for characters in s: 
        if characters in comma:
            out = s.replace(characters,".")
    return out 

#Task 13
def total_digits(s):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    total = 0 

    for i in s: 
        if i.isdigit() == True: 
            total +=  int(i)
    return total 

#Task 14
def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    d = 0
    counter = 0 
    if s1 == s2:
        d = 0   
    elif len(s1) != len(s2):
        d = -1      
    for i in s1:
        if len(s1) == len(s2) and i not in s2:
            counter += 1  
        d = counter
    return d

#Task 15 
def calculate(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    result = 0 
    num1 = int(expr[0])
    num2 = int(expr[4])
    
    operator = expr[2]

    if operator == "+":
        result = num1 + num2 
        
    elif operator == "-":
        result = num1 - num2
        
    elif operator == "*":
        result = num1 * num2
        
    elif operator == "/":
        if(num2 == 0):
            result = None
        else:
            result = num1 / num2
            
    elif operator == "%":
        if(num2 == 0):
            result = None
        else:
            result = num1 % num2
        
    return result 
    