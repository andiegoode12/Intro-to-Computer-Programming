"""
Andie Goode
10/13/15
Nested:Drawing a Pyramid(PY)
"""
#output statement
print("Drawing a Pyramid")
#prompt user for height of pyramid
height=int(input("Enter the height of the pyramid: "))
#spaces will always equal height-1
spaces= height-1
#set stars equal to 1
stars = 1
#iterate height times
for i in range (height):
    #iterate spaces times adding that many spaces to the left
    for j in range(spaces):
        #output space
        print(" ",end="")
    #iterate stars times adding that many stars to the center
    for k in range(stars):
        #output star
        print("*",end="")
    #iterate spaces times adding that many spaces to the right
    for l in range(spaces):
        #output space
        print(" ",end="")
    #output empty string
    print("")
    #subtract 1 from spaces each iteration
    spaces-=1
    #add 2 to stars each iteration
    stars+=2
