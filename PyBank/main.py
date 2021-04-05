
#import modules to read file

import os
import csv

#set path file
csvpath = os.path.join("Resources", "budget_data.csv")

#Set lists and variables
dates = []
revenue = []
changerevenue = []

#open csv file and skip first row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

#iterate in each row to append unique dates
    for row in csvreader:
        
        #calculate total dates
        dates.append(row[0])

        #calculate total revenue        
        revenue.append(int(row[1]))

#iterate in row[1] to find changes in everymonth
    for i in range(len(revenue)-1):
        changerevenue.append(float(revenue[i+1]-revenue[i]))

    #print(changerevenue)

#calculations
total_dates = len(dates)
total_revenue = int(sum(revenue))
averagechange = round((sum(changerevenue) / (len(dates)-1)),2) 
greatestincrease = max(changerevenue)
greatestdecrease = min(changerevenue)
max_index = changerevenue.index(greatestincrease)+1
min_index = changerevenue.index(greatestdecrease)+1


#print 
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {total_dates}')
print(f'Total: ${total_revenue}')
print(f'Average Change: ${averagechange}')
print(f'Greatest Increase in Profits: {dates[max_index]} ${greatestincrease}')
print(f'Greatest Decrease in Profits: {dates[min_index]} ${greatestdecrease}')

#create a text file

outputpath = os.path.join("analysis", "financialanalysis.txt")
with open(outputpath, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('------------------------\n')
    txtfile.write(f'Total Months: {total_dates}\n')
    txtfile.write(f'Total: ${total_revenue}\n')
    txtfile.write(f'Average Change: ${averagechange}\n')
    txtfile.write(f'Greatest Increase in Profits: {dates[max_index]} ${greatestincrease}\n')
    txtfile.write(f'Greatest Decrease in Profits: {dates[min_index]} ${greatestdecrease}\n')
