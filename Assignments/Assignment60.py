"""
Andie Goode
11/13/15
Dictionary:Sales Manager
"""

info = {}
#add each key and corresponding value inputed by user to dictionary 'info'
while True:
    name = input("Enter salesperson or QUIT to quit:")
    if name == "QUIT":
       break
    sales = int(input("Enter the number of sales: "))
    info[name] = sales
#set max_name to empty string
max_name = ""
#set max_val to really small number
max_val = -100000
#find max_value and corresponding name
for key in info:
    if info[key] > max_val:
        max_name = key
        max_val = info[key]
#set min_name to empty string       
min_name = ""
#set min_val to really small number
min_val = 100000
#find min_val and corresponding name
for key in info:
    if info[key] < min_val:
        min_name = key
        min_val = info[key]
#make list of all values
allsales = list(info.values())
#variables equal to 0
total = 0
num = 0
#calculate the total of all sales and number of salespersons
for i in allsales:
    total += i
    num += 1
#calculate average
avg = total/num

        
#output the maximum sales and corresponding salesperson
print('The person with the most sale is',max_name,'with',max_val,'sales')
#output the minumum sales and corresponding salesperson
print('The person with the least sale is',min_name,'with',min_val,'sales')
#ouptut average sales and salespersons whose sales were below average
print('The person(s) performing below the average of',str(int(avg)),'is(are):')
#print names of those whose sales are below average
for i in info:
    #if sales is less than average then output name
    if info[i] < avg:
        print(i)
    
