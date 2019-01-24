"""
Andie Goode
10/7/15
While:Prime Numbers(PY)
"""
#output statement
print("Prime Numbers")
#prompt user for number
num = int(input("Enter an integer: "))
#set x equal to 2 
x = 2
#loop while num is greater than or equal to x
while num >= x:
    # print prime if the remainder of num/x is zero
    # this means that if 1<x<num it is not prime
    if num%x == 0:
        #output statement
        print("Not Prime")
        break
    #set x equal to x plus one
    x+=1
    # if num equals x
    # and no previous value x gave remainder of 0 when divided into num
    # then it is Prime
    if num==x:
        #output statement
        print("Prime")
        break
