"""
Andie Goode
10/14/15
Nested:Perfect Numbers(PY)
"""
#output statement
print("Perfect Numbers")
#prompt user for limit
n = int(input("Enter the limit: "))
#set total and divisor equal to 0
total = 0
divisor = 0
#set perfect equal to empty string
perfect = ""
#loop from 1 to n+1
for i in range (1,(n+1)):
    #reset divisor equal to 0 at beginning of each new iteration
    divisor=0
    #loop from 1 to i
    for j in range (1,i):
        #if the remainder of i/j = 0 then set divisor equal to divisor + j
        if i%j==0:
            divisor+=j
    #if divisor = i then it is perfect
    if divisor==i:
        #this will print each perfect number in the limit
        #if perfect is an empty string then convert i to sting and add to perfect
        if perfect=="":
            perfect+=str(i)
        #if not add perfect to a comma and i converted to string and set perfect equal to it
        else:
            perfect+= (","+str(i))
#output statement
print("The perfect numbers are:",perfect)
            



            
        
        
   
