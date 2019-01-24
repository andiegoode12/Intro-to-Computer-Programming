"""
Andie Goode
11/5/15
Lists: Names
"""
#prompt user for first names
print('Enter some first names. Enter "quit" to quit.')
first = input("")
#create list of first names and add all inputs to it
L1 = []
L1.append(first)
while first != 'quit':
    first = input('')
    if first != 'quit':
        L1.append(first)
#sort list of first names alphabetically
L1.sort()

#prompt user for middle names      
print('Enter some middle names. Enter "quit" to quit.')
middle = input("")
#create list of middle names and add all inputs to it 
L2 = []
L2.append(middle)
while middle != 'quit':
    middle = input('')
    if middle != 'quit':
        L2.append(middle)
#sort list of middle names alphabetically
L2.sort()

#prompt user for last names      
print('Enter some last names. Enter "quit" to quit.')
last= input("")
#create list of last names and add all inputs to it 
L3 = []
L3.append(last)
while last != 'quit':
    last= input('')
    if last != 'quit':
        L3.append(last)
#sort lsit of last names alphabetically
L3.sort()

#output statements
print("")
print('Full name\t\tInitials')
print('--------------------------------')
#find which loop is the shortest
if len(L1)<=len(L2) and len(L1)<=len(L3):
    loop = len(L1)
if len(L2)<=len(L1) and len(L2)<=len(L3):
    loop = len(L2)
if len(L3)<=len(L1) and len(L3)<=len(L2):
    loop = len(L3)
#loop in range length of shortest list
for i in range(loop):
    #grab initial of each name(first,middle,last)
    init1 = L1[0]
    init1 = init1[0]
    init2 = L2[0]
    init2 = init2[0]
    init3 = L3[0]
    init3 = init3[0]
    #set name equal to first middle last
    name = (L1[0]+' '+L2[0]+' '+L3[0])
    #set initial equal to each single initial added together
    initial = (init1.upper()+init2.upper()+init3.upper())
    #output name and initial
    print(name+'\t'+initial)
    #pop first item from lists
    L1.pop(0)
    L2.pop(0)
    L3.pop(0)
   
# if each list is not empty then output the leftovers
if L1 != []:
    print("")
    print('Leftover first names:')
    for i in L1:
        print(i)
    
if L2 != []:
    print("")
    print('Leftover middle names:')
    for i in L2:
        print(i)
    
if L3 != []:
    print("")
    print('Leftover last names:')
    for i in L3:
        print(i)
    
