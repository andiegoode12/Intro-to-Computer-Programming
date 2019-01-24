"""
Andie Goode
9/23/15
Decision Structures:Derangements
"""

print("This program determines the number of letters or numbers that are in their correct place.")
#set total to zero
total = 0
#collecting values from user
char_1 = input("Enter character 1: ")
char_2 = input("Enter character 2: ")
char_3 = input("Enter character 3: ")
char_4 = input("Enter character 4: ")
char_5 = input("Enter character 5: ")

#if char_1 is 1 or a then add 1 to total
if char_1 == "1" or char_1 == "a":
    total = total + 1
#if not leave total the same
else:
    total = total
#if char_2 is 2 or b then add 1 to total
if char_2 == "2" or char_2 == "b":
    total= total + 1
#if not leave total the same
else:
    total = total
#if char_3 is 3 or b then add 1 to total
if char_3 == "3" or char_3 == "c":
    total= total + 1
#if not leave total the same
else:
    total = total
#if char_4 is 4 or b then add 1 to total
if char_4 == "4" or char_4 == "d":
    total= total + 1
#if not leave total the same
else:
    total = total
#if char_5 is 5 or b then add 1 to total
if char_5 == "5" or char_5 == "e":
    total= total + 1
#if not leave total the same
else:
    total = total

#outputting total
print("The number of letters or numbers in their correct places is",total)
