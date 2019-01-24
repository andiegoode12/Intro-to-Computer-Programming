"""
Andie Goode
12/8/15
Recursion: Raise to Power
"""
#create recursive function pwr
def pwr(X,Y):
    # if Y == 0 return 1
    if Y == 0:
        return 1
    else:
        # increment Y
        Y -= 1
        #return X multiplied by call pwr(X,Y)
        return X * pwr(X,Y)

def main():
    print("This program calculates exponential values.")
    #prompt user to enter base and power
    base = int(input("Enter the base: "))
    exp = int(input("Enter the power: "))
    #output solution
    print(str(base) +'^'+ str(exp),'=',pwr(base,exp))
#call main
main()
