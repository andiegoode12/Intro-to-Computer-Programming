"""
Andie Goode
9/23/15
IF: Lawn-mowing service (PY)
"""
#collecting values from user
length = int(input("Enter the lawn's length:"))
width = int(input("Enter the lawn's width:"))
#outputting length and width of lawn
print("For a",length,"by",width,"lawn")
#calculating area of lawn
area = length * width
weeks = 20
#outputting area of lawn
print("(Total area of",area,"square feet)")
#if area is <= 400 the fee is $25
if area < 400:
    fee = 25
    print("The weekly fee is: $"+str(fee))
#if area is between 400 and 600 the fee is $35
elif 400 <= area < 600:
    fee = 35
    print("The weekly fee is: $"+str(fee))
#if area is >= 600 the fee is $50
elif area >= 600:
    fee = 50
    print("The weekly fee is: $"+str(fee))
#calculate and output the total fee
print("For the "+str(weeks)+"-week season, the total is: $"+str(weeks * fee))
