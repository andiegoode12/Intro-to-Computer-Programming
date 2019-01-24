"""
Andie Goode
9/17/15
Population Growth
"""
#set numerator and denominator equal to zero
numerator = 1
denominator = 1
#set pi and approx equal to 0
pi = 0
approx = 0
#collect value iterations from user
iterations = int(input("Enter the number of iterations: "))
#for loop in range iterations
for i in range(iterations): 
 approx=approx+(numerator/denominator)
 numerator=numerator*-1 
 denominator=denominator+2
#multiply approx by four
pi = approx * 4
#output pi rounded to 3 decimals
print("The approximation of pi is", round(pi,3))
        
        
