"""
Andie Goode
10/22/15
Strings: Dot Products
"""
total = 0
#output statement
print("This program computes the dot product of two vectors.")
print("Enter the elements of the first vector or -1 to quit:")
#set variable equal to zero
num_a = 0
#prompt user for integer
vector1 = int(input(""))
#convert vector1 to string
a = str(vector1)
#loop until user input is -1
while vector1 != -1:
    #prompt user for another integer
    vector1 = int(input(""))
    #add 1 to variable num_a
    num_a += 1
    #add a comma and vector1 converted to a string to variable a and set equal
    a += "," + str(vector1)
#remove ',-1' from string a
a = a[0:len(a)-3]
#output statement
print("Enter the elements of the second vector or -1 to quit:")
#set variable equal to zero
num_b = 0
#prompt user for integer
vector2 = int(input(""))
#convert vector2 to string
b= str(vector2)
#loop until user input is -1
while vector2 != -1:
    #prompt user for another integer
    vector2 = int(input(""))
    #add one to variable num_b
    num_b += 1
    #add a comma and vector2 converted to a string to variable b and set equal
    b += "," + str(vector2)
#remove ',-1' from string b
b = b[0:len(b)-3]
#strip the commas out of the strings
a=a.strip(",")
b=b.strip(",")
#then split the numbers at the commas
a=a.split(",")
b=b.split(",")
#if the number of digits in vector1 and vector2 are not equal then print statement
if num_a != num_b:
    print("This dot product could not be computed.")
#if they are equal
else:
    #loop len(a) times
    for i in range(len(a)):
        #calculate dot product by adding the product of the numbers at position i in each string 
        total += (int(a[i]) * int(b[i]))
    #output dot product
    print("The dot product of these two vectors is "+str(total)+".")

