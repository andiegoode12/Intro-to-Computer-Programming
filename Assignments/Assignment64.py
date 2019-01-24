"""
Andie Goode
11/28/15
Function:Balanced Parentheses(PY)
"""
#create function
def CheckBalance(S):
    #if number of ( is same as number of ) then balanced
    if S.count('(') == S.count(')'):
        x = 'String Balanced'
    #otherwise it is unbalanced
    else:
        x = 'String Unbalanced'
    return x
#create main function
def main():
    #prompt user for string
    s = input("Enter a string: ")
    #call function CheckBalance with argument s
    ans = CheckBalance(s)
    #output answer
    print(ans)
#call main function
main()
