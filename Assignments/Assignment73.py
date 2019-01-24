"""
Andie Goode
12/8/15
Recursion:Palindromes
"""
#create function is Palindrome
def isPalindrome(string):
    #make string all lowercase
    string = string.lower()
    #if string is only one character of less then return true
    if len(string) <= 1:
        return True
    #if the first and second characters are the same then call isPalindrome again
    elif string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    #else return false
    else:
        return False

    
#create main function
def main():
    print("This program tests if strings are palindromes.")
    #prompt user to enter a string until they enter quit
    #and call ispalindrome for each string
    word = input("Enter a string: ")
    while word != 'quit':
        if isPalindrome(word) == True:
            print(word,"is a palindrome.")
        else:
            print(word,"is not a palindrome.")
        word = input("Enter a string: ")
#call main
main()
