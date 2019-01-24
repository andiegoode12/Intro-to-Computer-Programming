"""
Andie Goode
11/10/15
Dictionary:Student Enrollment
"""

D = {'CS150':20, 'CS250':10, 'CS270':30, 'CS300':24, 'CS350':11}
#output statement
print("This program checks enrollment")
#prompt user for class name
classname = input('Enter the class name or QUIT to quit: ')
#while input is not 'QUIT'
while classname != 'QUIT':
    #if classname is not 'QUIT'
    if classname != 'QUIT':
        #if name input no in Dictionary
        if classname not in D:
            #output statement and prompt user for new class name
            print('Class not found!')
            classname = input('Enter the class name or QUIT to quit: ')
        #if name is in the dictionary
        else:
            #prompt user for the current enrollment
            enroll = int(input("Enter current enrollment: "))
            #calculate the number of spots left
            numspots = D[classname] - enroll
            #output classname and number of spots left
            print(classname,'has',numspots,'seat(s) available')
            #prompt user for new classname
            classname = input('Enter the class name or QUIT to quit: ')
    # if classname is 'QUIT' then break
    else:
        break

    
