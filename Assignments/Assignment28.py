"""
Andie Goode
10/7/15
While Loop:Squarer
"""
#output statement
print("This program squares numbers. Enter a positive integer to square or -1 to quit.")
#prompt user for number to square or sentinel
num = int(input("Enter a positive integer or -1: "))
#loop as long as num is not -1
while num != -1:
    #calculate the square of num
    square = num*num
    #output square of num
    print(num,"squared is",square)
    #prompt user for another number to square or sentinel
    num = int(input("Enter a positive integer or -1: "))
