"""
Andie Goode
10/13/15
Nested Loops: Pick Up Sticks
"""
#prompt user for initial number of sticks in the pile
num_sticks = int(input("How many sticks would you like there to be in the pile? Choose a number between 5 and 50: "))
#if num_sticks is outside of the range 5-50 then invalid try again
while(num_sticks<5 or num_sticks>50):
     print("That number is not between 5 and 50. Please try again.")
     num_sticks = int(input("How many sticks would you like there to be in the pile? Choose a number between 5 and 50: "))
#if the remainder of num_sticks and 4 is not 1
if num_sticks%4!=1:
     #computer goes first, output statement
     print("I will go first.")
     #Until there are no more sticks left, loop
     while num_sticks!=0:
          #output statement and current number of sticks
          print("")
          print("There are currently",num_sticks,"sticks on the pile.")
          print("Current status of the pile:")
          print("*"+"|"*num_sticks+"*")
          print("")
          #pick up certain number of sticks depending on what the remainder is
          #set num_sticks equal to itself minus number of sticks picked up
          if num_sticks%4==0:
               print("I will pick up 3 sticks.")
               num_sticks-=3
          if num_sticks%4==3:
               print("I will pick up 2 sticks.")
               num_sticks-=2
          if num_sticks%4==2:
               print("I will pick up 1 stick.")
               num_sticks-=1
          
          print("")
          #if there is only 1 stick left then make everything in sentence singular
          if num_sticks==1:
               print("There is currently",num_sticks,"stick on the pile.")
          #if there are more than one sticks left then make everything in sentence plural
          else:
               print("There are currently",num_sticks,"sticks on the pile.")
          #output statement and current number of sticks    
          print("Current status of the pile:")
          print("*"+"|"*num_sticks+"*")
          print("")
          #prompt user for number of sticks to pick up
          pick = int(input("How many sticks would you like to pick up? "))
          #while user choices number that is not 1,2,3 or then number is greater than the number of sticks
          while (pick <= 0 or pick > 3) or pick> num_sticks:
               #output invalid choice and prompt user for new number until number is valid
               print("Invalid choice. Please try again.")
               pick = int(input("How many sticks would you like to pick up? "))
          #set num_sticks equal to itself minus the number chosen     
          num_sticks-=pick
     #ouput empty string and statemnt     
     print("")
     print("You picked up the last stick. I won!")
#if the remainder of num_sticks/4 is 1     
else:
    #user goes first,output statement 
    print("You can go first.")
    print("")
    #while there are sticks in the pile
    while num_sticks>0:
          #if there is only 1 stick left then make everything in sentence singular
          if num_sticks==1:
               print("There is currently",num_sticks,"stick on the pile.")
          #if there are more than one sticks left then make everything in sentence plural     
          else:
               print("There are currently",num_sticks,"sticks on the pile.")
          #output statement and current number of sticks     
          print("Current status of the pile:")
          print("*"+"|"*num_sticks+"*")
          print("")
          #prompt user for number of sticks to pick up
          pick = int(input("How many sticks would you like to pick up? "))
          #while user choices number that is not 1,2,3 or then number is greater than the number of sticks
          while (pick <= 0 or pick >3) or pick> num_sticks:
               #output invalid choice and prompt user for new number until number is valid
               print("Invalid choice. Please try again.")
               pick = int(input("How many sticks would you like to pick up? "))
          #if valid number chosen is equal to the number of sticks               
          if pick==num_sticks and 0<pick<=3:
               #output statement, computer winns
               print("")
               print("You picked up the last stick. I won!")
               #break the loop
               break
          #set num_sticks equal to itself minus the number chosen
          num_sticks -= pick
          #output statement and current number of sticks 
          print("")
          print("There are currently",num_sticks,"sticks on the pile.")
          print("Current status of the pile:")
          print("*"+"|"*num_sticks+"*")
          print("")
          #pick up certain number of sticks depending on what the remainder is
          #set num_sticks equal to itself minus number of sticks picked up
          if num_sticks%4==0:
               print("I will pick up 3 sticks.")
               num_sticks-=3
          if num_sticks%4==3:
               print("I will pick up 2 sticks.")
               num_sticks-=2
          if num_sticks%4==2:
               print("I will pick up 1 stick.")
               num_sticks-=1
          print("")
 
