"""
Andie Goode
11/5/15
Lists: Dot Products
"""

total = 0
#output statement
print("This program computes the dot product of two vectors.")
print("Enter the elements of the first vector or -1 to quit:")

num_a = 0
#prompt user for vector1
vector1 = int(input(""))
L = []
#add input to list
L.append(vector1)
#add input to list until input ==-1
while vector1 != -1:
    vector1 = int(input(""))
    if vector1 != -1:
        num_a += 1
        L.append(vector1)
    else:
        break


#output statement
print("Enter the elements of the second vector or -1 to quit:")

num_b = 0
#prompt user for vector2
vector2 = int(input(""))
#add input to list2
L2 = []
L2.append(vector2)
#add inputs to list2 until input == -1
while vector2 != -1:
    vector2 = int(input(""))
    if vector2 != -1:
        num_b += 1
        L2.append(vector2)
    else:
        break

# if the vectors are not the same length then can not compute
if num_a != num_b:
    print("This dot product could not be computed.")
#else calclute dot product
else:
    for i in range(len(L)):
        
        total += (L[i] * L2[i])
    #output dot product
    print("The dot product of these two vectors is "+str(total)+".")

