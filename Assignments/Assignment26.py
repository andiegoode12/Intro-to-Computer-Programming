"""
Andie Goode
10/6/15
While Loop:Add Until Sentinel
"""
total = 0
#output print statement to screen
print("Enter a list of numbers, using a negative number to indicate that you are done.")
#collecting number from user
num = float(input("Enter a number: "))
#loop every time num is greater than or equal to zero
while num >= 0:
    # running total
    total += num
    #collecting number from user
    num = float(input("Enter a number: "))
print("")
#output total
print("The total is", total)
