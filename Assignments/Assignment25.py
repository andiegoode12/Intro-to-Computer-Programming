"""
Andie Goode
9/24/15
IF: Paycheck Calculator (PY)
"""

print("This program computes your paycheck")
#collecting total hours worked from user
hours = float(input("Enter the total hours: "))
#if hours is 40 or less
if hours<=40:
    wage = 7.50
    #calculate pay when wage is 7.50
    pay = hours * wage
    #output pay rounded to 2 decimals
    print("Your paycheck is {0:.2f}".format(round(pay,2)))
#if hours is > 40 
elif hours > 40:
    wage = 7.50
    wage2 = 11.25
    #calculate pay for extra hours with wage 11.25 and add to wage of 40 hours
    pay = ((hours-40)*wage2) + (40*wage)
    #output pay rounded to 2 decimal
    print("Your paycheck is {0:.2f}".format(round(pay,2)))
