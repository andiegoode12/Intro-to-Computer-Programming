"""
Andie Goode
9/9/15
Warehouse Carpeting(PY)
"""
#outputting statement
print("Welcome to Discount Carpet Warehouse")
#collecting length from user
length = float(input("Enter the room's length (in feet): "))
#collecting width from user
width = float(input("Enter the room's width (in feet): "))
#calculating area
area = length * width
#outputting area rounded to 2 decimals
print("The floor space is %0.2f square feet." % area)
#calculating cost to carpet room
cost = 70.00 + (1.50*area)
#outputting cost to carpet a room with the calculated area
print("The cost to carpet this floor is: $%0.2f." % cost)
