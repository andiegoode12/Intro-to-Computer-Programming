"""
Andie Goode
9/17/15
Ball Bounce
"""
#setting variables to zero
x = 0
y = 0
total_height = 0
#collecting values from user
height = float(input("Enter the height from which the ball is dropped: "))

bounce= float(input("Enter the bounciness index of the ball: "))

bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

#for loop in range bounces calculating total height
for distance in range(bounces):
    x=height
    height = height * bounce
    y = height
    total_height = total_height + x + y
print("")
#outputting total height
print ("Total distance traveled is:",total_height,"units.")

