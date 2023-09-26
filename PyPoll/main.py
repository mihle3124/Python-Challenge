import os
import csv


#PyPoll Analysis

#Open path to the csv file
PyPoll_csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#Declaring Neccessary Variables
Total_Votes = 0
Candidates_Name = {}
Candidate_Votes = {}

#Open Path and read csv file
with open(PyPoll_csvpath, encoding='UTF-8')as PyPoll_csvfile:
    PyPoll_csvreader = csv.reader(PyPoll_csvfile, delimiter=",")

    #Skip Header
    next(PyPoll_csvreader)
    for row in PyPoll_csvreader:
        #Total Votes count
        Total_Votes +=1
        #Setting Candidate Name
        Candidates_Name = row[2]
        if Candidates_Name not in Candidate_Votes:
            Candidate_Votes[Candidates_Name] = 0
        #Vote count for each candidate
        Candidate_Votes[Candidates_Name] += 1

#Print title and Total Votes
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {Total_Votes}")
print("-------------------------------------")

#Defining the Winner variables
Winner = ""
Winner_Votes = 0

for Candidate_name, Votes in Candidate_Votes.items():
    #Calculating the percent
    Percentage = round(Votes/Total_Votes*100, 3)
    #Print Names by votes and percentage
    print(f"{Candidate_name}: {Percentage}% ({Votes})")
    if Votes > Winner_Votes:
        Winner = Candidate_name
        Winner_Votes = Votes

#Print the Winner Candidate
print("-------------------------------------")
print(f"Winner: {Winner}")
print("-------------------------------------")


          
        









