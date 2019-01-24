"""
Andie Goode
12/7/15
Recursion:Something In Common(PY)
"""
#create gcd function
def gcd(a,b):
    if b == 0:
        return a
    else:
       return gcd(b,a%b)
#create main function
def main():
    #prompt user to enter values a and b
    a = int(input("Please enter the value of a: "))
    b = int(input("Please enter the value of b: "))
    #output solution
    print("gcd("+str(a)+','+str(b)+') = '+str(gcd(a,b))+'.')
#call main
main()
