#calculating time from seconds

"""Inputs a number of seconds from the user and then calculate the number of hours, minutes, and remaining seconds. 
Print them seperated by "-".
For example if the user types 3750 seconds as an input the script should print 1 - 2 - 30"""
#example
h = 3750 // (60*60)
m = 3750 % (60*60) // 60
s = 3750 % (60*60) % 60
print(h, '-', m, '-', s)

userInput = int(input("Enter the time in seconds: "))
h = userInput // (60*60)
m = userInput % (60*60) // 60
s = userInput % (60*60) % 60
print(h, '-', m, '-', s)