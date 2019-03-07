#Libraries to read CSVs and processing path routes
import os
import csv
import operator

#Path of the file
csvpath = "election_data.csv"
output_path = "election_results.csv"
#Path for file with the results
#output_path = "Results_budget_data.csv"

count_votes = 0
candidates = []
uniq_candidates = []
candid_act = ""
totals = []
total_perc = []
count_v_cand = 0
count_c = 0
d= 0.0

#CSV file processing...
with open(csvpath, newline='') as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

  # Read the header and skip it
   csv_header = next(csvreader,None)
   
 # 1-The total number of votes cast
 # 2-A complete list of candidates who received votes
   for row in csvreader:

      if row[0] is not None:
        count_votes += 1
        candidates.append(row[2])

#Sorted list of candidates    
candidates.sort()
#Lenght of list of candidates
no_candidates = len(candidates)

# 3-Calculate total votes by candidate
for c_act in candidates:
    count_c += 1
    if count_v_cand == 0:
      cand = c_act
      count_v_cand = 1
    else:
      if cand == c_act:
        count_v_cand += 1
        cand = c_act
      else:
        totals.append([cand, count_v_cand])
        count_v_cand = 1
        cand = c_act
    if count_c == no_candidates:
      totals.append([cand, count_v_cand])

# 4-Distinct names of candidates
for numb in range(len(candidates)):
      
  candid = candidates[numb]
  count_v_cand += 1
  if candid != candid_act:
      uniq_candidates.append(candidates[numb])
  candid_act = candid

# 5-Calculate total percentages
for x in totals:
    d = round(((int(x[1])/count_votes)*100))
    total_perc.append([x[0],d])

# 6-Winner of election based on number of votes
g = sorted(totals, key=operator.itemgetter(1))
f = g[-1]

#Formatting the results for printing
for tp, tot in zip(total_perc, totals):
    tp.append(tot[1])

# 7-Print the results to the terminal
print("--------------------------------------------")
print("ELECTION RESULTS")
print("--------------------------------------------")
print("Total number of votes: " + str(count_votes))
print("--------------------------------------------")
print("--------------------------------------------")
print("Candidates who received votes: " )
print(*uniq_candidates, sep = ", ")
print("--------------------------------------------")
#Print the sublists with the results with percentage and totals
for j in total_perc:
  print(str(j[0]) + ": " + str(j[1]) + " %  " + " (" + str(j[2]) + ")" + "\n")

print("--------------------------------------------")
print("The winner is: " + str(f[0]))
print("--------------------------------------------")

# 8-Write the results to file
with open(output_path, 'w', newline='') as csvfile:

     # Initialize csv.writer
     csvwriter = csv.writer(csvfile, delimiter=',')

     # Write the first row (title)
     csvwriter.writerow(['Election Results'])

     # Write the contents
     csvwriter.writerow(['Total number of votes:', count_votes])
     csvwriter.writerow(['Candidates who received votes:', uniq_candidates])
     for m in total_perc:
          csvwriter.writerow(str(m[0]) + ": " + str(m[1]) + " %  " + " (" + str(m[2]) + ")")
        #print(str(j[0]) + ": " + str(j[1]) + " %  " + " (" + str(j[2]) + ")" + "\n")
#     csvwriter.writerow(['Average changes:', average_changes])
#     csvwriter.writerow(['Greatest increase in profit:', date_increase, max_increase])
#     csvwriter.writerow(['Greatest decrease in profi:', date_decrease, max_decrease])
     print("File with results written!!")

      
      
   


