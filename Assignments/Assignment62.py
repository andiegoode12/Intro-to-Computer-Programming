"""
Andie Goode
11/28/15
Functions: Volume of a Sphere
"""
#set global variable
PI = 3.14159
#create function sphereVolume
def sphereVolume(radius):
    #calculate volume of sphere and return answer
    ans = (4/3) * PI * (radius**3)
    return ans
#create function main 
def main():
    print("This program computes the volume of a sphere.")
    #prompt user for radius
    r = float(input("Enter the radius: "))
    #call function with argument r
    vol = sphereVolume(r)
    #output volume rounded to 2 decimal places
    print("The volume is %0.2f" %vol)
#call main function
main()
    
