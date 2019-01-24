"""
Andie Goode
9/9/15
Math:Metric Conversion
"""

#outputting statement
print("This program converts from feet and inches to centimeters.")
#collecting feet from user
Ft = float(input("Enter feet: ")) 
#collecting inches from user
inch_1 = float(input("Enter inches: ")) 
#convert feet to inches
inch_2 = Ft*12
#add inches and convert to centimeters
cm = (inch_1 + inch_2) * 2.54
#output blank space
print("")
#outputting the length in centimeters rounded to 2 decimal places
print("The length is",format(cm,'.2f'),"cm.")
