"""
Andie Goode
10/26/15
File:Display Content
"""
#prompt user for filename
name = input("Enter input file: ")
#open file
file = open(name,'r')

#set lines to read file
lines = file.read()

#remove any blank lines
remove = lines.rstrip()

#split file into list of each seperate line
line = remove.split('\n')

#output number of lines which is length of variable line
print("Total number of line is",len(line))

#prompt user for which line to read
linenum = int(input("Enter the line number to be displayed or -1 to quit: "))

#loop while linenum is not equal to -1
while linenum != -1:
    #if linenum is greater than 0 or less than or equal to len(linenum) then print the specified line and prompt user for new line number
    if (linenum>0 and linenum <= len(line)):
        print(line[int(linenum)-1])
        linenum = int(input("Enter the line number to be displayed or -1 to quit: "))
    #else output invalid and prompt user for new line number
    else:
        print("Invalid line number")
        linenum = int(input("Enter the line number to be displayed or -1 to quit: "))

#close file
file.close()
