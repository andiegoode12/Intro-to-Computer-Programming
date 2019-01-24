"""
Andie Goode
10/22/15
Nested:Radar
"""
#prompt user for inuts
dimension = int(input("dimension: "))
coordinate = input("coordinate: ")
bearing = input("bearing: ")
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

        




