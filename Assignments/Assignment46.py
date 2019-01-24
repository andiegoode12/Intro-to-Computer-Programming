"""
Andie Goode
10/26/15
File I/O: Average Numbers
"""
#output statement
print("This program averages numbers inside a given file.")
#prompt user for filename
name = input("Enter a filename: ")
#loop while name is not equal to 'quit'
while name != 'quit':
    #open file
    file = open(name,'r')
    #set variable equal to read file
    lines = file.read()
    #split file into list of each seperate line 
    line = lines.split('\n')
    #set/reset variables equal to 0
    total = 0
    num = 0
    #for loop to calculate sum of all numbers 
    for i in range(len(line)):
        total += int(line[i])
        num+=1
    #close file
    file.close()
    #average numbers
    avg = total/num
    #output average rounded to 2 decimal places
    print("The average is %0.2f" %avg)
    #prompt user for another filename
    name = input("Enter a filename: ")
    
