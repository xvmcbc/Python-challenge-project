#Libraries to read CSVs and processing path routes
import os
import csv

#Path of the file
csvpath = "budget_data.csv"
#Path for file with the results
output_path = "Results_budget_data.csv"

count_months = 0
net_amount = 0
p_ant = 0
tot_change = 0
record = []
date = []

#CSV file processing...
with open(csvpath, newline='') as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

  # Read the header and skip it
   csv_header = next(csvreader,None)
   
 # 1-Analyze the total number of months included in the dataset 
 # 2-The net total amount of "Profit/Losses" over the entire period
 # 3-The average of the changes in "Profit/Losses" over the entire period
 # 4-The greatest increase in profits (date and amount) over the entire period
 # 5-The greatest decrease in losses (date and amount) over the entire period
   for row in csvreader:

    if row[0] is not None:
      count_months += 1
      net_amount += int(row[1])
    
    if count_months >= 2:
      date.append(row[0])
      record.append((int(row[1])) - p_ant)

    p_ant = int(row[1])

#Total of changes / number of changes
average_changes = round(sum(record)/(len(record)),2)

#Max increase and decrease in profits
max_increase = max(record)
max_decrease = min(record)
date_increase = date[record.index(max_increase)]
date_decrease = date[record.index(max_decrease)]

#Printing the results to the terminal
print("Number of months : " + str(count_months))  
print("Net Total amount : $" + str(net_amount))   
print("Average changes  : $" + str(average_changes))    
print("Greatest increase in profit: " + str(date_increase) + " " + str(max_increase))
print("Greatest decrease in profit: " + str(date_decrease) + " " + str(max_decrease))


#Write the results to file
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (title)
    csvwriter.writerow(['Results Analysis Budget Data'])

    # Write the contents
    csvwriter.writerow(['Number of months:', count_months])
    csvwriter.writerow(['Net Total amount:', net_amount])
    csvwriter.writerow(['Average changes:', average_changes])
    csvwriter.writerow(['Greatest increase in profit:', date_increase, max_increase])
    csvwriter.writerow(['Greatest decrease in profi:', date_decrease, max_decrease])
    print("File with results written!!")

      
      
   


