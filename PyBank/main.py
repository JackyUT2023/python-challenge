# First we'll import the os module
# This will allow us to create file paths across operation systems
import os

# Module for reading CSV files
import csv
csvpath=os.path.join('Resources','budget_data.csv')

# Lists to store Date data
Date = []
Net_Profit_Losses = []
Change_Net_Profit_Losses = []


# With open(csvpath) as csvfile:
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader=csv.reader(csvfile,delimiter=",")

    # Read the header row first (skip this step if there is no hearder)
    csv_header=next(csvreader)

    for row in csvreader:
        #Add Date and Net_Profit_Losses
        Date.append(row[0])
        Net_Profit_Losses.append(int(row[1]))

# Use For Loop to input every single month variables into [Date] array, then use "len" to count the number of months
Total_Months=len(Date)
# Same For Loop to input every Net_Profit_Losses variables into [Net_Profit_Losses] array, then use "sum" to get a total number.
Total_Net_Profit_Losses=sum(Net_Profit_Losses)
# -----------------------------------------------------------------------------------------------------------------------------------------

# Use For Loop to calculate the change of Net_Profit_Losses on each month (current value-previous value), then generate a new array called [Change_Net_Profit_Losses]:
    # Attention: Because there is no previous value for the first month, it should start with index 1, not 0.
for index in range(1,len(Net_Profit_Losses)):

    Change_Net_Profit_Losses.append(int(Net_Profit_Losses[index])-int(Net_Profit_Losses[index-1]))

# Import "mean" module, then apply it to [Change_Net_Profit_Losses]
from statistics import mean
Avg_Change=round(mean(Change_Net_Profit_Losses),2)
# -----------------------------------------------------------------------------------------------------------------------------------------

# What we are going to do next is to zip [Date] and [Change_Net_Profit_Losses] together into a list. 
# However, their size is different. We have to avoid the first month from [Date], since there was no change. So we generate a new array, [Date_Modified].
Date_Modified=[]
for index2 in range(1,len(Date)):
    Date_Modified.append(Date[index2])

a = max(Change_Net_Profit_Losses)
b = min(Change_Net_Profit_Losses)
Ziplist=list(zip(Date_Modified,Change_Net_Profit_Losses))

# Use For Loop + If, to find the right rows variables, which match the max.Change_Net_Profit_Losses and the min.Change_Net_Profit_Losses.
for row in Ziplist:
    if row[1] == a:
        Greatest_Increase_in_Profits = (row[0] + " ($" + str(row[1])+")")
    elif row[1] == b:
        Greatest_Decrease_in_Profits = (row[0] + " ($" + str(row[1])+")")
# -----------------------------------------------------------------------------------------------------------------------------------------
# Print Result as below.

print("Financial Analysis")
print("------------------------------------------------------------")

print("Total Months: " + str(Total_Months))
print("Total: $" + str(Total_Net_Profit_Losses))
print("Average Change: $" + str(Avg_Change))
print("Greatest Increase in Profits: " + Greatest_Increase_in_Profits)
print("Greatest Decrease in Profits: " + Greatest_Decrease_in_Profits)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Export txt file
# Specify the file to write to
output_path = os.path.join("analysis", "PyBank Financial Analysis Result.txt")

lines=["Financial Analysis",
        "------------------------------------------------------------",
        " ",
        "Total Months: " + str(Total_Months),
        "Total: $" + str(Total_Net_Profit_Losses),
        "Average Change: $" + str(Avg_Change),
        "Greatest Increase in Profits: " + Greatest_Increase_in_Profits,
        "Greatest Decrease in Profits: " + Greatest_Decrease_in_Profits]

# Open the file using "write" mode. and use for loop to write the lines.
with open(output_path, 'w') as txtfile:
    for line in lines:
        txtfile.write (line)
        txtfile.write ('\n')
