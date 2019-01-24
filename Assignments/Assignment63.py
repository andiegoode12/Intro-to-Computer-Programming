"""
Andie Goode
11/28/15
Function:Representation Converter
"""
#create dictionary
D = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
     'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
#create function repConvert
def repConvert(rep,base):
    #set exponent equal to len of rep - 1
    exponent = len(rep)-1
   #set decial equal to 0
    decimal=0
    #for loop range length of representation
    for i in range (len(rep)):
        #value equals value associated with key rep at position i
        value = D[rep[i]]
        #calculate decimal
        decimal += value * (base**exponent)
        #subtract 1 from exponent
        exponent -= 1
    #return decimal 
    return decimal    
#create function main
def main():
    print("This program converts any representation to decimal")
    #prompt user for representation and base
    rep = input("Enter a representation:")
    base = int(input("Enter a base:"))
    #call function with arguments rep, base
    ans = repConvert(rep,base)
    #output decimal equivalent
    print("Decimal equivalent:" + str(ans))
    
#call function main               
main()
