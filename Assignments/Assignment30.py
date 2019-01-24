"""
Andie Goode
10/7/15
While:Euclid GCD (PY)
"""
#prompt user for smaller and larger number
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
#loop until smaller is 0
while smaller !=0 :
    #calculate the remainder
    remainder = larger%smaller
    #set larger equal to smaller
    larger = smaller
    #set smaller equal to the remainder
    smaller = remainder
#ouput GCD
print("The greatest common divisor is", larger)
