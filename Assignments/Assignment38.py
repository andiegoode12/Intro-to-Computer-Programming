"""
Andie Goode
10/22/15
String:Universal Product Code Check Digit Verification Program
"""
#prompt user for bar code
code = input("Enter a bar code: ")
#set variables to zero
add_odd = 0
add_even = 0
#set for loop to i in range zero to length of bar code skipping everyother position
for i in range(0,len(code)-1,2):
    #set variable odd to number at position i
    odd = code[i]
    #add odd converted to integer to add_odd and set it equal
    add_odd += int(odd)
#multiply add_odd by 3
oddtotal = add_odd*3
#set for loop i in range 1 to 1 less than length of bar code skipping every other position
for i in range(1,len(code)-1,2):
    #set variable even to number at position i
    even = code[i]
    #add even converted to integer to add_even and set it equal
    add_even += int(even)
#add add_even and oddtotal and calculate the remainder when divided by 10
rem =(add_even+oddtotal)%10
#subtract remainder from 10
check = 10-rem
#if check is the same as the final digit of the bar code then Correct
if check == int(code[-1]):
    print("Correct Check Digit")
#if check is not the same as the final digit of the bar code then Incorrect
else:
    print("Incorrect Check Digit")


    

    
