"""
Andie Goode
10/13/15
Nested Loops: Burger Order
"""
#prompt user for values
burgers = int(input("How many burgers do you want? "))
items = int(input("How many items would you like on your burger? "))
#set b equal to 1 in order to set interval
b=1
#loop until b is not less than or equal to the number of burgers
while b<(burgers+1):
    #set i equal to 1 in order to set interval
    i=1
    #output each burger and its items
    print("Burger",b)
    #loop until i is not less that or equal to the number of items
    while i<(items+1):
        #output each item on the burger
        print("Item #"+str(i))
        #increase i by 1
        i+=1
    #increase b by 1    
    b+=1
    #add empty line
    print("")
#output statement
print("Order complete.")
