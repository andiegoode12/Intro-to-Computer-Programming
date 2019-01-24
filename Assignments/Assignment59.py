"""
Andie Goode
11/10/15
Dictionary:Days in a Month
"""
D = {'january':31,'february':28,'march':31,'april':30,'may':31,'june':30,
     'july':31,'august':31,'september':30,'october':31,'november':30,'december':31}
#Output statement
print("This program tells you how many days there are in a month")
#prompt user for month
month = input("Enter the month you want to know or QUIT to quit: ")
#loop while month is not QUIT
while month != 'QUIT':
    #if month is not QUIT
    if month != 'QUIT':
        #make new variable equal to month but all lower case
        monthL = month.lower()
        #if lower month (monthL) is in the dictionary then print number of days in month
        if monthL in D:
            print(month,'has',D[monthL],'days')
        #if it is not in the dictionary then output the below statement
        else:
            print("That month is not part of the year!")
        #prompt user for another month
        month = input("Enter the month you want to know or QUIT to quit: ")
    #if month is QUIT, then break the loop
    else:
        break


