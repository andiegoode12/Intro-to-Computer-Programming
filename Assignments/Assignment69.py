"""
Andie Goode
12/7/15
Recursion: Fibonacci Sequence
"""
#create function fib
def fib(n):
    #fib at 0 == 0
    if n == 0:
        return 0
    #fib at 1 and 2 == 1
    if n == 1 or n == 2:
        return 1
    #if fib not 0,1,2 then calculate next in sequence
    else:
        return (fib(n-1) + fib(n-2))
#create main function
def main():
    print("This program calculates numbers in the Fibonacci sequence.")
    #prompt user to enter location to calculate fib
    x = int(input("Which place in the sequence do you want to calculate? "))
    #output fibonaccie sequence at location x
    print("Fibonacci("+str(x)+") is",fib(x))
#call main
main()
