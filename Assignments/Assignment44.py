"""
Andie Goode
10/25/15
File I/O: File Display
"""
#output statement
print("This program displays numbers read from a file.")
#open file and read
file = open('numbers.txt','r')
lines = file.read()
#split each line at line break
line = lines.split('\n')
#loop through length of line to print each number in the file
for i in range(len(line)):
    print('Number:',line[i])
    
