"""
Andie Goode
11/5/15
Lists: Scoring Key
"""
#list of correct answers
Correct = ['B','D','A','A','C','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']
#prompt user for file name
filename = input('Enter a filename: ')
print("")
#open file and read
file = open(filename,'r')
#split file into list of each line
lines = file.read()
answer = lines.split('\n')

print('Contents of',filename)
#output number and answer given
for i in range(len(answer)):
    print(str(i+1)+':',answer[i])

numright = 0
probnumright = ''
numwrong = 0
probnumwrong = ''

for i in range(len(Correct)):
    #if the answer is correct then keep count of how many are correct and which answers where correct
    if answer[i] == Correct[i]:
        numright += 1
        probnumright += str(i+1)+','
    ##if the answer is incorrect then keep count of how many are incorrect and which answers where incorrect
    if answer [i] != Correct[i]:
        numwrong += 1
        probnumwrong += str(i+1)+','
#remove trailing comma from each string       
if probnumright.endswith(','):
    probnumright = probnumright[:-1]
if probnumwrong.endswith(','):
    probnumwrong = probnumwrong [:-1]
#ouput final values    
print("Total correctly answered questions:",numright)
print("Questions that were answered correctly:",probnumright)
print("Total incorrectly answered questions:",numwrong)
print("Questions that were answered incorrectly:",probnumwrong)
#calculate and output pass or fail
L = probnumright.split(',')
if len(L) >= 15:
    print("This exam receives a passing score.")
else:
    print("This exam receives a failing score.")

    
