#Import Dependencies

import os
import csv

#path to the csvfile

csvpath = os.path.join('budget_data.csv')

#initializing the variables 
total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Open the CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

# calculating the total number of months and total revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        # Calculate change from this month to previous months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        
        #calculating the greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        #calculating the greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
      
    # calculating the average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # printing all values
    print("Financial Analysis")
    print("----------------------")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print("average_change:"+ str (average_change))
    print(f"Greatest_Increase_in Profits:",greatest_increase_month, max(changes))
    print(f"Greatest_Decrease_in Profits:",greatest_decrease_month, min(changes))



   