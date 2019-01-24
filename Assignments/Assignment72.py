"""
Andie Goode
12/7/15
Recursion:Finding the largest number(PY)
"""
#create rlarge function
def rlarge(L):
    if len(L) == 1:
        return L[0]
    else:
        x = rlarge(L[1:])
        if L[0] > x:
            return L[0]
        else:
            return x
        
        
        
        
#create main function
def main():
    #prompt user to enter number of values and what they are
    x = int(input("How many values?"))
    L=[]
    for i in range(x):
        val = int(input(">>"))
        L.append(val)
    print("The maximum is",rlarge(L))
#call main
main()
