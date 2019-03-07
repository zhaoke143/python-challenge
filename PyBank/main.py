import os
import csv

# Set File Path
csv_path = os.path.join('Resources', 'budget_data.csv')
output_path = "Output.txt"

# Read the File
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    # create lists
    month = []
    profit = []
    profit_change = []
    
    # loop and update lists
    for row in csvreader:
        month.append(row[0])
        profit.append(int(row[1]))
    # loop and update profit change
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
                      
# find min and max change and monthly change
greatest_increase = max(profit_change)
greaest_decrease = min(profit_change)
greatest_month_increase = profit_change.index(max(profit_change))+1
greatest_month_decrease = profit_change.index(min(profit_change))+1

# Print to terminal
print(f"Financial Analysis")
print(f"------------------------")
print(f"Total Months:{len(month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month[greatest_month_increase]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {month[greatest_month_decrease]} (${(str(greaest_decrease))})")      

# Save to a new .txt file
with open(output_path, 'w') as file:
    file.write(f"Financial Analysis \n")
    file.write(f"------------------------ \n")
    file.write(f"Total Months:{len(month)} \n")
    file.write(f"Total: ${sum(profit)} \n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)} \n")
    file.write(f"Greatest Increase in Profits: {month[greatest_month_increase]} (${(str(greatest_increase))}) \n")
    file.write(f"Greatest Decrease in Profits: {month[greatest_month_decrease]} (${(str(greaest_decrease))}) \n")
    