"""
Andie Goode
9/16/15
For Loop: Add n
"""
#set total = 0
total = 0
#collecting how many numbers I should add from the user
input_number = int(input("How many numbers should I add? "))
#setting how many iterations in for loop
for value in range(input_number):
    #collecting values to add from user
    input_value = float(input("Enter a number: "))
    #calculating total
    total = total + input_value
#outputting empty string
print("")
#outputting what the total is rounded to 1 decimal
print("The total is",round(total,1))

