"""
Andie Goode
9/17/15
Salary
"""
#set x equal to 0
x=0
#collecting values from user
salary = float(input("Enter the starting salary: $"))
percent_incr = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))
print("Year\tSalary\n")
#for loop range 1 through years plus 1 calculating salary per year
for year in range(1,years+1):
    print(year,"\t",round(salary,2))
    salary = salary + (salary * (percent_incr/100))


