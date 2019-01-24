"""
Andie Goode
11/10/15
Dictionary:Average Temperature
"""
#prompt user for temperatures each day of the week
monday = int(input('Enter the temperature for Monday: '))
tuesday = int(input('Enter the temperature for Tuesday: '))
wednesday = int(input('Enter the temperature for Wednesday: '))
thursday = int(input('Enter the temperature for Thursday: '))
friday = int(input('Enter the temperature for Friday: '))
saturday = int(input('Enter the temperature for Saturday: '))
sunday = int(input('Enter the temperature for Sunday: '))
#add inputs and keys to dictionary
D = {}
D['Monday'] = monday
D['Tuesday'] = tuesday
D['Wednesday'] = wednesday
D['Thursday'] = thursday
D['Friday'] = friday
D['Saturday']= saturday
D['Sunday'] = sunday
#make list of values
temps = list(D.values())
#set a maximum and minimum number
minimum = 100000000
maximum = -1000000000
#calculate maximum temperature for the week
for i in D:
    if D[i] > maximum:
        maximum = D[i]
        maxi = i
#calculate minimum temperature for the week
for i in D:
    if D[i] < minimum:
        minimum = D[i]
        mini = i
total = 0
num = 0
#find sum of all temps for the week
for i in range(len(temps)):
    total += temps[i]
    num +=1
#calculate average temperature 
avg = total/num
#output max, min,and average
print("The maximum temperature of "+str(maximum)+'F was recorded on',maxi)
print("The minimum temperature of "+str(minimum)+'F was recorded on', mini)
print("The average temperature for the week is:",str(int(avg)) +'F')
