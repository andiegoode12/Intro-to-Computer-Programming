"""
Andie Goode
11/10/15
Dictionary:Hex to Bin
"""
hextobin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101',
            '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011',
            'C':'1100','D':'1101','E':'1110','F':'1111'}
#ouput statement
print("This program converts hex to binary")
#prompt user for text to convert 
hexa = input("Enter a hex representation:")
#output statement with next thing printed on same line
print("The binary representation is: ", end = '')
#convert input text to binary by finding key and associated value
for ch in hexa:
    print(hextobin[ch], end ='')
