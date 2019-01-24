"""
Andie Goode
10/28/15
File:Radar
"""
#prompt user for file
name = input("file: ")
#open file
file = open(name,'r')
#read file
lines = file.read()
#strip file of line break
values = lines.strip('\n')
#strip file of empty strings
values = values.rstrip()
#split file at commas
values = values.split(',')
#dimension equals first value in list
dimension = int(values[0])
print('dimension:',dimension)
#coordinate equals the second and third values in list
coordinate = values[1]+','+values[2]
print('coordinate:',coordinate)
#bearing equals fourth value in list
bearing = values[3]
print('bearing:',bearing)
#split string coordinates at comma
coordinates = coordinate.split(',')
#set x coordinate to first value in list coordinates
xcoordinate = int(coordinates[0])
#set y coordinate to second value in list coordinates
ycoordinate = int(coordinates[1])
#set variables equal to zero
xpos = 0
ypos = 0
#if bearing is in southern half then add ycoordinate to dimensions
if bearing[0] == 's':
    ypos = dimension + ycoordinate
#if bearing in northern half then subtract ycoordinate from dimensions
if bearing[0] == 'n':
    ypos = dimension - ycoordinate
#if bearing in right half then add xcoordinate to dimensions
if bearing[1] == 'e':
    xpos = dimension + xcoordinate
#if bearing in left half then subtract xcoordinate from dimensions
if bearing[1] == 'w':
    xpos = dimension - xcoordinate
#print coordinate plane
for i in range((dimension*2)+1):
    for j in range ((dimension*2)+1):
        #if i is ypos and j is xpos then print the star in that spot
        if i == ypos and j == xpos:
            print('*', end = '')
        #otherwise continue printing the coordinate plane
        else:
            print("-",end="")
    print("")
#close file
file.close()
