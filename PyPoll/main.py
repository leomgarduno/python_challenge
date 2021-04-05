#import modules to read file

import os
import csv

#set path file
csvpath = os.path.join("Resources", "election_data.csv")


#Set lists
votes = []
candidatesdict =  {}

#open csv file and skip first row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    
#generate dictionary
    for i in csvreader:
        votes.append(i[0])
        candidate = i[2]
        vote = 1

        if candidate not in candidatesdict:
            candidatesdict[candidate] = vote
        else:
            candidatesdict[candidate] += 1 
        # x += 1
        # x = x+1

#print results and generate for loop to count votes inside the dictionary

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {len(votes)}')
print(f'-------------------------')

for candidate in candidatesdict:
        print(f'{candidate}: {((candidatesdict[candidate]/len(votes))*100):.3f}%, ({candidatesdict[candidate]})')

print(f'-------------------------')
winner = max(candidatesdict, key=candidatesdict.get) 
print(f'Winner: {winner}') 
print(f'-------------------------')


#create  a text file

outputpath = os.path.join("analysis", "electionresults.txt")
with open(outputpath, 'w') as txtfile:
    txtfile.write(f'Election Results\n')
    txtfile.write(f'-------------------------\n')
    txtfile.write(f'Total Votes: {len(votes)}\n')
    txtfile.write(f'-------------------------\n')
    for candidate in candidatesdict:
        txtfile.write(f'{candidate}: {((candidatesdict[candidate]/len(votes))*100):.3f}%, ({candidatesdict[candidate]})\n')
    txtfile.write(f'-------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write(f'-------------------------\n')




