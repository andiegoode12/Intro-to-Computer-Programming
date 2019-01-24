"""
Andie Goode
10/22/15
String:Morse Code
"""
#prompt user to convert to Morse code
word = input("Enter the text to be translated: ")
#convert all letters in string to lower case
words=word.lower()
#for loop goes through words and replaces each character with corresponding morse code
for i in words:
    words = words.replace(".","  ")
    words = words.replace("!","  ")
    words = words.replace("?","  ")
    words = words.replace("a",".-")
    words = words.replace("b","-...")
    words = words.replace("c","-.-.")
    words = words.replace("d","-..")
    words = words.replace("e",".")
    words = words.replace("f","..-.")
    words = words.replace("g","--.")
    words = words.replace("h","....")
    words = words.replace("i","..")
    words = words.replace("j",".---")
    words = words.replace("k","-.-")
    words = words.replace("l",".-..")
    words = words.replace("m","--")
    words = words.replace("n","-.")
    words = words.replace("o","---")
    words = words.replace("p",".--.")
    words = words.replace("q","--.-")
    words = words.replace("r",".-.")
    words = words.replace("s","...")
    words = words.replace("t","-")
    words = words.replace("u","..-")
    words = words.replace("v","...-")
    words = words.replace("w",".--")
    words = words.replace("x","-..-")
    words = words.replace("y","-.--")
    words = words.replace("z","--..")
    #Output converted string converted to morse code
    print("The morse code equivalent is:",words)
    #end loop
    break
    
