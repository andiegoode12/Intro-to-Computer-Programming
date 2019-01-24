"""
Andie Goode
12/8/15
Recursion:Towers of Hanoi
"""
#create function towersolve
def towersolve(n):
    # if there are 0 discs then return 0
    if n == 0:
        return 0
    #else call towersolve for (n-1) multiplied by two and add 1
    else:
        return((towersolve(n-1)*2) + 1)


#create main
def main():
    #prompt user to enter how many discs
    x = int(input("How many discs: "))
    #call towersolve and ouptut solution
    print("Tower of Hanoi with",x,"discs require", towersolve(x),"steps")
#call main
main()
