import os
import csv
csvpath = os.path.join('Resources','election_data.csv')


Voter_ID = []
Candidate_Name=[]
Candidate_Name_Unique=[]

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)


#Use for loop to seperate Voter_ID coloum and candidate names coloum from csvfile, then make list of each of them. 
    for row in csvreader:
        Voter_ID.append(row[0])
        Candidate_Name.append(row[2])

#Use len function to count Voter_ID, and get the result of Total Votes.
Total_Votes=len(Voter_ID)

#Use for loop again in the list of candidate names to filter out the duplicated value and get the list of candidates.
for Names in Candidate_Name:
    if Names not in Candidate_Name_Unique:
        Candidate_Name_Unique.append(Names)

# Since we don't know how many candidates yet, if we don't run above script, so we have to use while loop to backcount the candidate name, votes and percentage.
Last_Index_of_Candidate = len(Candidate_Name_Unique)-1
Initial_Index=-1
Total_Votes_Received_List=[]
Percentage_of_Votes_won_List=[]
Candidate_Vote_List=[]
while Last_Index_of_Candidate != Initial_Index:
     Votes=Candidate_Name.count(str(Candidate_Name_Unique[Last_Index_of_Candidate]))
     Percentage=Votes/len(Candidate_Name)
     Total_Votes_Received_List.append(Votes)
     Percentage_of_Votes_won_List.append(format(Percentage,".3%"))
     
     Last_Index_of_Candidate -=1

     Temp_Value=str(Candidate_Name_Unique[Last_Index_of_Candidate+1]+": "+str(format(Percentage,".3%"))+" ("+str(Votes)+")")
     Candidate_Vote_List.append(Temp_Value)

#Make the lists as a tuple, so that it's easier to find the winner by looking up the coresponding votes received.  
Candidate_Vote_Tuple=list(zip(Candidate_Name_Unique, Percentage_of_Votes_won_List, Total_Votes_Received_List))

Most_Votes_Won=max(Total_Votes_Received_List)
for row in Candidate_Vote_Tuple:
    if row[2] == Most_Votes_Won:
        Winner = row[0]

# Print Result
# --------------------------------------------------------------------------------------------
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_Votes))
print("-------------------------")
print(f"Candidates List: {Candidate_Name_Unique}")  

print(f"{Candidate_Vote_List}")
print("-------------------------")
print("Winner: "+Winner)
print("-------------------------")

#Output the text file.
# --------------------------------------------------------------------------------------------

output_path = os.path.join("analysis", "PyPoll Analysis Result.txt")

lines=["Election Results","-------------------------","Total Votes: " + str(Total_Votes),"-------------------------"]

Candidate_Names=[Candidate_Name_Unique]

Candidate_Votes_List=[Candidate_Vote_List]

with open(output_path, 'w') as txtfile:
    for line in lines:
        txtfile.write (line)
        txtfile.write ('\n')
    for Candidate_Names in Candidate_Name_Unique:
        txtfile.write (Candidate_Names)
        txtfile.write ('\n')
    txtfile.write ('\n')
    for Candidate_Votes_List in Candidate_Vote_List:
        txtfile.write (Candidate_Votes_List)
        txtfile.write ('\n')
    txtfile.write ('\n')
    txtfile.write ("-------------------------")
    txtfile.write ('\n')
    txtfile.write("Winner: "+Winner)
    txtfile.write ('\n')
    txtfile.write("-------------------------")