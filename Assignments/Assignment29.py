"""
Andie Goode
10/8/15
While Loop: Input Validation
"""
#prompt user for ID number
ID = int(input("Enter your ID: "))
#set tries equal to 0
tries = 0
#loop until False
while True:
    # if the id is valid print statement
    if (0<= ID <= 199) or (1200<= ID <= 1350) or (ID == 2376):
        print("ID accepted.")
        break
    #add 1 to tries 
    tries = tries + 1
    # if try to submit more than 5 times, lock out of system
    if tries == 5:
        print("Invalid ID, you are locked out of the system.")
        break
    # if tries is less than five prompt for ID number again
    print("Invalid ID, you may try again.")
    ID = int(input("Enter your ID: "))
            
