"""
Andie Goode
10/22/15
Strings: Text Analysis
"""
#output statement
print("This program analyzes text. Enter text or enter \"quit\" to quit.")
#prompt user for text
text = input("Please enter some text: ")
#set variable equal to zero
text1 = 0
#as long as text input by user is not 'quit'
while (text != 'quit') and (text1 != 'quit'):
    #add empty string to variable text
    text+=""
    #prompt user for next line of text
    text1 = input("Please enter some text: ")
    #set text equal to text plus ';' plus text1
    text += ";" + text1
#remove the ' quit' from text
text = text[0:-5]
#set variable equal to zero
upper = 0
#loop len(text) times
for i in range (len(text)):
    #set variable a equal to text at position i
    a = text[i]
    #if a is uppercase then add 1 to varible upper
    if a.isupper():
        upper +=1
#output number of uppercase letters in text
print("There are",upper,"uppercase letters in this text.")
#set variable equal to zero
lower = 0
#loop len(text) times
for i in range (len(text)):
    #set variable a equal to text at position i
    a = text[i]
    #if a is lowercase then add 1 to variable lower
    if a.islower():
        lower +=1
#output number of lowercase letters in text
print("There are",lower,"lowercase letters in this text.")
#set variable equal to zero
digit = 0
#loop len(text) times
for i in range (len(text)):
    #set variable a equal to text at position i
    a = text[i]
    #if a is a digit then add 1 to variable digit
    if a.isdigit():
        digit +=1
#output number of digits in text
print("There are",digit,"digits in this text.")
#count the whitespace characters in text
whitespace = text.count(' ')
#output number of whitespace characters in text
print("There are",whitespace,"whitespace characters in this text.")
