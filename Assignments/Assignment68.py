"""
Andie Goode
11/28/15
Function: Left Standing(redo)
"""
#create function left_standing
def left_standing(people,kill_rate):
    #calculate people left and return
    ppl = (people - (people * (kill_rate/100)))
    return ppl
#create main function
def main():
    print("Castle defense")
    #prompt user for inputs
    a = float(input("Enter number of enemies: "))
    b = float(input("Enter catapult kill percentage: "))
    c = float(input("Enter archer kill percentage: "))
    #calculate left standing after catapults
    x = left_standing(a,b)
    #calculate left standing after archers
    y = left_standing(x,c)

    if (y - int(y)) > .5:
        y = int(y) + 1
    else:
        y = int(y)
        
    print("Total enemies remaining:",y)
main()
