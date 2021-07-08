'''
-----------------------------------------------
Lab Ten, Task 1
-----------------------------------------------
Author: Nishant Tewari
ID:     190684430
Email:  tewa4430@mylaurier.ca
__updated__ = "2021-07-04"
-----------------------------------------------
'''
#Task 1 
def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    fh.seek(0)
    result = []
    line = fh.readline()
    counter = 0
    
    while line != "" and counter != n: 
        line = fh.readline()
        counter += 1    
    if line != "" :
        line = line.strip()
        result = line.split(',')
    
    return result