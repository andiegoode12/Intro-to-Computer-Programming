"""
Andie Goode
11/29/15
Functions: Surface Area of a Sphere
"""
#set global variable
PI = 3.14159
#create function sphereArea
def sphereArea(radius):
    #calculate area of sphere and return answer
    ans = 4 * PI * (radius**2)
    return ans
#create function main    
def main():
    print("This program computes the surface area of a sphere.")
    #prompt user for radius
    r = float(input("Enter the radius: "))
    #call function with argument r
    area = sphereArea(r)
    #ouput surface area rounded to 2 decimal places
    print("The surface area is %0.2f" %area)
    
#call main function
main()
