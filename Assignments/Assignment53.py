"""
Andie Goode
11/5/15
Lists: Date Printer
"""

Month = ['January','February', 'March','April','May','June','July','August','September','October','November','December']

print('This program converts dates.')
#prompt user for date to convert
date = input("Please enter a date in the form mm/dd/yyyy: ")

#split date into list at/
datelist = date.split('/')

newlist = []
#convert first two values in datelist to integer and add to newlist
for i in range(len(datelist)-1):
    newlist.append(int(datelist[i]))
#add remaining value in datelist to newlist
for i in range(2,len(datelist)):
    newlist.append(datelist[i])
convert = ''
#convert by finding corresponding month to number given
for i in range(len(Month)):
    if i+1 == newlist[0]:
        convert = convert + Month[i]
#finish conversion
convert += ' '+str(newlist[1])+', '+newlist[2]
print('The converted date is',convert+'.')
