import os
import csv

#PyBank Analysis

PyBank_csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#Declaring Neccessary Variables
Total_Months = 0
Net_Profit = 0
Total_Change = 0
Biggest_Increase = ["",0]
Biggest_Decrease = ["",0]

#Open Path and read csv file
with open(PyBank_csvpath, encoding='UTF-8') as PyBank_csvfile:
    PyBank_csvreader = csv.reader(PyBank_csvfile, delimiter=",")

    #Skip Header
    next(PyBank_csvreader)
    #Skip First Row to indicate that Profit Changes start after first row
    First_Data_Row = next(PyBank_csvreader)
    
    #Define Variable for Previous Change in Profit
    Previous = int(First_Data_Row[1])
    #Count Total Months
    Total_Months += 1
    #Caculate Total Profit
    Net_Profit += Previous 
    
    for row in PyBank_csvreader:
        #Count Months
        Total_Months +=1
        #Setting current profit
        Current = int(row[1])
        #Setting Total Profit
        Net_Profit += Current
        #Calculating the Change of profit
        Change = Current - Previous
        Total_Change += Change
        Previous = Current
        
        #Calculating the Greatest Increase in Profits
        if Change > Biggest_Increase[1]:
            Biggest_Increase[0] = row[0]
            Biggest_Increase[1] = Change
        #Calculating the Greatest Decrease in Profits
        if Change < Biggest_Decrease[1]:
            Biggest_Decrease[0] = row[0]
            Biggest_Decrease[1] = Change 
    
    #Calculating the Average Change
    Average_Change = Total_Change / (Total_Months-1)

#Printing the Analysis
print("Financial Analysis")        
print("---------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Net_Profit}")
print(f"Average Change: ${round(Average_Change, 2)}")
print(f"Greatest Increase in Profits: {Biggest_Increase[0]} (${Biggest_Increase[1]})")
print(f"Greatest Increase in Profits: {Biggest_Decrease[0]} (${Biggest_Decrease[1]})")







          
        









