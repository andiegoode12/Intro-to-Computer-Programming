"""
Andie Goode
10/22/15
Nested:Octal Numbers
"""
#print statements
print("Enter 1 to convert from octal to decimal.")

print("Enter 2 to convert from decimal to octal.")
#prompt user for input 1 or 2
enter = int(input(""))
#if user input 1, convert octal to decimal
if enter == 1:
    #prompt user for octal digit
    octal = input("Enter a string of octal digits: ")
    #set the exponent to the length of string octal - 1
    exponent = len(octal)-1
    #set decimal equal to 0
    decimal=0
    #loop i in range length of octal
    for i in range (len(octal)):
        #find digit at i postion and set equal to value
        value = octal[i]
        #calculate decimal number
        decimal += (int(value)*(8**exponent))
        #subtract 1 from exponent
        exponent -= 1
    #ouput decimal
    print("The integer value is",decimal)
#if user input 2, convert decimal to octal
if enter == 2:
    #prompt user for decimal integer
    decimal = int(input("Enter a decimal integer: "))
    #set octal equal to empty string
    octal = ""
    #loop while decimal is greater than 0
    while decimal >0:
        #set remainder equal to the remainder of decimal value divided by base 8
        remainder = decimal%8
        #add remainder converted to string to octal and set equal
        octal += str(remainder)
        #find quotient of decimal and base 8 and set decimal equal
        decimal = decimal//8
    #flip the string octal because adding remainder in reverse order
    octal = octal[::-1]
    #output octal
    print("The octal representation is",octal)
