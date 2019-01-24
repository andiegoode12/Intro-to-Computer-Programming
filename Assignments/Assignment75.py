"""
Andie Goode
12/8/15
Recursion:Counting Occurence(PY)
"""
#create function counting
def counting(S,ch):
    #make string lower case
    S = S.lower()
    #if string is empty then return 0
    if len(S) == 0:
        return 0
    #if the last character in the string is equal to the character you are looking for
    if S[-1] == ch:
        #call counting with last character removed from string and add 1
        return counting(S[:-1],ch) + 1
    else:
        #call counting with last character removed from string
        return counting(S[:-1],ch)
    
        

#call main
def main():
    #prompt user to enter string and character
    string = input("Enter a string: ")
    char = input("Which character to look for: ")
    print("The number of occurences of",char,"is",counting(string,char))

main()
