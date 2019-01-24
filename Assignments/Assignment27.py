"""
Andie Goode
10/7/15
While Loop: Average until Sentinel
"""
#output statemnt
print("This program averages numbers.")
#prompt user for number
num = float(input("Number: "))
#set variables equal to zero
count = 0
total = 0
#loop as long as num is not equal to -1
while num!= -1:
    #if num is positive 
    if num >= 0:
        #calculate running total of all input numbers
        total += num
        #total of how many numbers inputed
        count += 1
        #prompt user for another number
        num = float(input("Number: "))
    #if num is negative
    else:
        #prompt user for another number
        num = float(input("Number: "))
#calculate the average
avg = total/count
#output the average
print("")
print("The average is {0:.2f}".format(round(avg,2)))
