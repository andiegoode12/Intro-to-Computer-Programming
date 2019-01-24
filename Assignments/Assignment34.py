"""
Andie Goode
10/13/15
Nested:Drawing a Pyramid(PY)
"""
#output statement
print("Drawing a Reverse Pyramid")
#prompt user for height of inverted pyramid
height=int(input("Enter the height of the pyramid: "))
#set stars equal to the length of the base
stars = (2*height)-1
#loop iterates 'height' times
for i in range (height):
    #loop iterates i times adding i spaces to left side
    for j in range(i):
        #output space
        print(" ",end="")
    #loop iterates stars times adding k stars to center
    for k in range(stars):
        #ouput star
        print("*",end="")
    #loop iterates i times adding i spaces to right side
    for l in range(i):
        #output statement
        print(" ",end="")
    #output empty string
    print("")
    #subtract 2 from stars at the end of loop
    stars-=2
