"""
Andie Goode
10/13/15
Loop:Numbers and Squares(PY)
"""
#prompt user for upper and lower limits
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
#set i equal to lower limit
i=lower
#output statement
print("Numbers: ",end="")
#loop while i is between upper and lower or equal to upper and lower
while lower<=i<=upper:
    #loop until i is greater than or equal to upper
    if i<upper:
        #output list of integers with comma after
        print(str(i)+",",end="")
    else:
        #output final integer without comma after
        print(str(i))
    #add 1 to i    
    i+=1
#set i equal to lower again    
i=lower
#output statement
print("Squares: ",end="")
#loop while i is between upper and lower or equal to upper and lower
while lower<=i<=upper:
    #loop until i is greater than or equal to upper
    if i<upper:
        #output list of squares of i with comma after 
        print(str(i*i)+",",end="")
    else:
        #output list of final square of i without comma after
        print(str(i*i))
    #add 1 to i
    i+=1
