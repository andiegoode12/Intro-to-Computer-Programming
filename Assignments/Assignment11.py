"""
Andie Goode
9/9/15
Minutes to Hours(PY)
"""
#outputting statement
print("This program converts minutes to hours")
#collecting minutes from user
minutes = int(input("Enter the total minutes: "))
#converting minutes to hours
hours = minutes//60
#calculating remaining minutes
rem_minutes = minutes%60
#outputting hours and remaining minutes
print(minutes,"minutes is",hours,"hours and",rem_minutes,"minutes")
