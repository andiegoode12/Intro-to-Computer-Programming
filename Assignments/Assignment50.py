"""
Andie Goode
11/5/15
Lists: Number Analysis
"""
#output statement
print('Please enter some numbers. Type \'q\' to quit.')
#prompt user for value
number = input('Enter a number: ')
L = []
total = 0
num = 0
#add number to list L
L.append(int(number))
#prompt user for number until quit and add those numbers to the list
while number != 'q':
    number = input('Enter a number: ')
    if number != 'q':
        L.append(int(number))
    else:
        L.append(number)
#remove q
L.remove('q')
#sort the list
L.sort()
#ouput lowest and highest numbers in the list
print('The lowest number is',L[0])
print('The highest number is',L[len(L)-1])
#calculate total of all numbers in list
for i in range(len(L)):
    total += int(L[i])
    num+=1
#calculate average
avg = total/num
#output total and average
print('The total of the numbers is',total)
print('The average of the numbers is %0.2f'%avg)
               
