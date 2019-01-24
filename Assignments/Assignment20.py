"""
Andie Goode
9/21/15
Decision Structures: Loan Approval
"""

print("This program determines whether you may get a loan.")
#prompting user for values income, cred_rate, coll
income = int(input("Please enter your income in dollars: "))
cred_rate = int(input("Please enter your credit rating: "))
coll =input("Please enter if you are using collateral (yes or no): ")
#create if statement with condition
if income>= 50000 and cred_rate >= 600 or coll=='yes':
    print("Approved!")
#if condition not met output below statement
else:
    print("We are sorry, but you are not approved.")
