
from functions import customer_record

fh = open("customers.txt", "r")

print("Find record n")

n = int(input("\nEnter a record number: "))

result = customer_record(fh, n)

print(result)

fh.close()