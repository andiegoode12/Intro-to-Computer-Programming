"""
Andie Goode
11/28/15
Function:Compute Price
"""
#create function drawers
def drawers():
    #prompt user for number of drawers and return d
    d = int(input("Enter number of drawers >> "))
    return d
#create function wood
def wood ():
    #prompt user for wood type
    w = input("Enter type of wood - m, o, or p >> ")
    #find what type of wood from initial and return x
    if w == 'm':
        x = 'mahogany'
    if w == 'o':
        x = 'oak'
    if w == 'p':
        x = 'pine'
    return x
#create function cost
def cost (w,d):
    #calculate cost based on wood type and number of drawers
    if w == 'pine':
        c = 100 + 30*d
    elif w == 'oak':
        c = 140 +30*d
    else:
        c = 180 + 30*d
    return c
#create function details
def details():
    #call function drawers
    d = drawers()
    #call function wood
    w = wood()
    #call function cost with arguments w and d
    c = cost(w,d)
    #output wood type and number of drawers
    print("You have ordered a",w,"desk with",d,"drawers")
    #output cost
    print("Total price is $"+str(c))
#create main function
def main():
    #call details function
    details()
#call main function
main()
