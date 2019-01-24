"""
Andie Goode
9/17/15
Population Growth
"""
# collecting values from user
organisms = int(input("Enter the initial number of organisms: "))
growth_rate = int(input("Enter the rate of growth [a real number > 1]: "))
hours_to_grow = int(input("Enter the number of hours to achieve the rate of growth: "))
hours = int(input("Enter the total hours of growth: "))
#subtract remainder from total hours
hours = hours - (hours%hours_to_grow)
#for loop range calculating total organisms
for i in range(0,hours,hours_to_grow):
    organisms = organisms * growth_rate
#outputting the total population
print("The total population is",organisms)
