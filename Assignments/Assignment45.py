"""
Andie Goode
10/26/15
File I/O: Line Numbers
"""
#prompt user for filename
name = input("Enter a filename: ")
print("")
#open file
file = open(name,'r')
#ouput statement
print("Contents of",name)
#set lines equal to reading file
lines = file.read()
#set line equal to a list of each seperate line
line = lines.split('\n')
#loop through the len of list line
for i in range(len(line)):
    #output line number, tab, and line at location i in list
    print(str(i+1)+':\t'+line[i])
#close file
file.close()
