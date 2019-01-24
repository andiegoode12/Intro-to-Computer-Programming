"""
Andie Goode
10/26/15
File::Morse Code Revisited
"""
#prompt user for filename
print("This program reads from file1.txt and translates the content to Morse code")
#open file
file = open('file1.txt','r')
#set variable to read file
lines = file.read()
#remove blank lines
remove = lines.rstrip()
#make everything lower case
lower = remove.lower()
#split into list of each seperate line
line = lower.split('\n')
#output number of lines
print("Total number of line is",len(line))
#prompt user for which line to translate
linenum = int(input("Enter the line number to be translated(1-7) or -1 to quit:"))
#while linenum is not equal to -1
while linenum != -1:
    #if linenum is not in range (1-7) then output invalid and prompt user for new line number
    if linenum <= 0 or linenum > len(line):
        print("Invalid line number")
        linenum = int(input("Enter the line number to be translated(1-7) or -1 to quit:"))
    else:
        #loop through line
        for i in line:
            #set variable equal to specified line
            morse = line[linenum-1]
            #convert each letter/space/punctuatin to corresponding morsecode
            morse = morse.replace(".","  ")
            morse = morse.replace("!","  ")
            morse = morse.replace("?","  ")
            morse = morse.replace("a",".-")
            morse = morse.replace("b","-...")
            morse = morse.replace("c","-.-.")
            morse = morse.replace("d","-..")
            morse = morse.replace("e",".")
            morse = morse.replace("f","..-.")
            morse = morse.replace("g","--.")
            morse = morse.replace("h","....")
            morse = morse.replace("i","..")
            morse = morse.replace("j",".---")
            morse = morse.replace("k","-.-")
            morse = morse.replace("l",".-..")
            morse = morse.replace("m","--")
            morse = morse.replace("n","-.")
            morse = morse.replace("o","---")
            morse = morse.replace("p",".--.")
            morse = morse.replace("q","--.-")
            morse = morse.replace("r",".-.")
            morse = morse.replace("s","...")
            morse = morse.replace("t","-")
            morse = morse.replace("u","..-")
            morse = morse.replace("v","...-")
            morse = morse.replace("w",".--")
            morse = morse.replace("x","-..-")
            morse = morse.replace("y","-.--")
            morse = morse.replace("z","--..")
            #Output string converted to morse code
            print("The morse code equivalent is:",morse)
            #end loop
            break
        #prompt user for new line number to convert
        linenum = int(input("Enter the line number to be translated(1-7) or -1 to quit:"))
#close file
file.close()
        

