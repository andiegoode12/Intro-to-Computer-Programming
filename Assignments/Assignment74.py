"""
Andie Goode
12/8/15
Recursion:Counting character(PY)
"""
#create function counting
def counting(S):
    #if list S is equal to the last character in the string return 0
    if S == S[:-1]:
        return 0
    else:
        return counting(S[:-1]) +1 #decrementing
    
    
#create main function
def main():
    #prompt user to enter a string
    x = input("Enter a string: ")he
    #call counting function
    print("The length of",x,"is",counting(x))
#call main
main()
