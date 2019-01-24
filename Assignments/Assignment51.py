"""
Andie Goode
11/5/15
Lists: Average Number of Words
"""
print("Please enter some sentences. Type \"quit\" on a line by itself to quit.")
total = 0
#prompt user for sentence
sentence = input('')
L = []
#split sentence at single spaces
K = sentence.split(' ')
#add list K to list L
L.append(K)
#prompt user for sentences until quit
while sentence != 'quit':
    sentence = input('')
    if sentence != 'quit':
        K = sentence.split(' ')
        L.append(K)
#remove empty string in each list within list L        
for i in range(len(L)):
    while "" in L[i]:
        L[i].remove("")

#calculate the total number of words in list L
for i in range(len(L)):
    for j in range(len(L[i])):
        total += 1
#caluclate average number of words by dividing total by len(L)
avg = total/len(L)
#ouput avg
print("These sentences have an average of %0.2f" %avg,"words.")
        
