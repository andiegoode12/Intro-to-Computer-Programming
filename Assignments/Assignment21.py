"""
Andie Goode
9/21/15
IF: Cheap Grocery(PY)
"""
cereal_total = 0
milk_total = 0
total = 0
print("This program saves money\n")

print("Store A")
#collecting values from user
cereal_A = float(input("Enter the price of a box of cereal: "))
milk_A = float(input("Enter the price of a quart of milk: "))
print("")
print("Store B")
#collecting values from user
cereal_B = float(input("Enter the price of a box of cereal: "))
milk_B = float(input("Enter the price of a quart of milk: "))
# if-else statement deciding which cereal price is lower and multiplying by 3
if cereal_A <= cereal_B:
    cereal_total = cereal_A * 3
else:
    cereal_total = cereal_B * 3
#if-else statement deciding which milk price is lower and multiplying by 2
if milk_A<= milk_B:
    milk_total = milk_A * 2
else:
    milk_total = milk_B * 2
#calculating total price
total = cereal_total + milk_total
#outputting the total price rounded to two decimal places
print("The total cost of three boxes of cereal and two quarts of milk is:",round(total,2))
