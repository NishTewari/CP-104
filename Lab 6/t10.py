from functions import treadmill

burnt_per_minute = float(input("Enter calories burned per minute: "))
start = int(input("Enter beginning number of minutes: "))
end = int(input("Enter ending number of minutes: "))
inc = int(input("Enter the increment in minutes: "))

print()
treadmill(burnt_per_minute,start,end,inc)