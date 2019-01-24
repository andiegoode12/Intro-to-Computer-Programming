"""
Andie Goode
9/16/15
Traveling Distance
"""
#collecting vehicle speed in mph from user
speed = int(input("What is the speed of the vehicle in mph? "))
#collecting hours the vehicle has traveled from user
total_hours = int(input("How many hours has it traveled? "))
#outputting Hour and Distance Traveled as headers for columns
print("Hour\tDistance Traveled")
#outputting line
print("-------------------------")
#set for loop with range from 1 to total_hours + 1
for hour in range(1,total_hours + 1):
    #calculating distance traveled
    total_dist = speed * hour
    #outputting distance and total distance in two seperate columns
    print(hour,"\t",total_dist)
    

    
