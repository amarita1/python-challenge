import csv


Original_List = []
Unique_List = []
Unique_List_Votes = []
Total_Votes = []
Counter_Votes = 1
Counter_Khan = 1
Counter_Correy = 1
Counter_Li = 1
Counter_0Tooley = 1

with open("python-challenge/PyPoll/Resources/election_data.csv", 'r') as input_file:
    csvreader = csv.reader(input_file)
    header = next(csvreader)

    for row in csvreader:
        #Create List of Candidates
        Original_List.append(row[2])

    #Create Candidate List with No Duplicates and Count Number of Votes per Candidate
    for x in Original_List:
        if x not in Unique_List:
            Unique_List.append(x)
        elif x == 'Khan':
            Counter_Khan += 1
        elif x == 'Correy':
            Counter_Correy += 1
        elif x == 'Li':
            Counter_Li += 1
        elif x == "O'Tooley":
            Counter_0Tooley += 1

    #Create List of Votes per Candidate 
    Unique_List_Votes.append(Counter_Khan)
    Unique_List_Votes.append(Counter_Correy)
    Unique_List_Votes.append(Counter_Li)
    Unique_List_Votes.append(Counter_0Tooley)

    #Combine No Duplicate Candidate List and Votes Per Candidate to Dictionary
    Combined_Unique = {Unique_List[i]: Unique_List_Votes[i] for i in range(len(Unique_List_Votes))} 

    #Find Percentage of Votes Won by Each Candidate (Candidate Votes/Total Votes)
    Total_Votes = sum(Unique_List_Votes)
    Percent_Khan = (Counter_Khan/Total_Votes)*100
    Percent_Corey = (Counter_Correy/Total_Votes)*100
    Percent_Li = (Counter_Li/Total_Votes)*100
    Percent_0Tooley = (Counter_0Tooley/Total_Votes)*100

    #Print Analysis
    print("Election Results")
    print("-----------------------------------")
    print(f"Total Votes: {Total_Votes}")
    print("-----------------------------------")
    print(f"Khan: {Percent_Khan: .3f}% ({Counter_Khan})")
    print(f"Correy: {Percent_Corey: .3f}% ({Counter_Correy})")
    print(f"Li: {Percent_Li: .3f}% ({Counter_Li})")
    print(f"O'Tooley: {Percent_0Tooley: .3f}% ({Counter_0Tooley})")
    print("-----------------------------------")

    Winner = max(Unique_List_Votes)

    for name, vote in Combined_Unique.items():
        if vote == Winner:
            print(f"Winner: {name}")
    print("-----------------------------------")

    with open("PyPollAnalysis.txt", "w") as outputfile:
        outputfile.write("Election Results\n")
        outputfile.write("-----------------------------------\n")
        outputfile.write(f"Total Votes: {Total_Votes}\n")
        outputfile.write("-----------------------------------\n")
        outputfile.write(f"Khan: {Percent_Khan: .3f}% ({Counter_Khan})\n")
        outputfile.write(f"Correy: {Percent_Corey: .3f}% ({Counter_Correy})\n")
        outputfile.write(f"Li: {Percent_Li: .3f}% ({Counter_Li})\n")
        outputfile.write(f"O'Tooley: {Percent_0Tooley: .3f}% ({Counter_0Tooley})\n")
        outputfile.write("-----------------------------------\n")
        outputfile.write(f"Winner: Khan\n")
        outputfile.write("-----------------------------------\n")



    
    




    
