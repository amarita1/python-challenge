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

print("Election Results")
print("-----------------------------------")
with open("python-challenge/PyPoll/Resources/election_data.csv", 'r') as input_file:
    csvreader = csv.reader(input_file)
    header = next(csvreader)

    for row in csvreader:
        Original_List.append(row[2])

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
Unique_List_Votes.append(Counter_Khan)
Unique_List_Votes.append(Counter_Correy)
Unique_List_Votes.append(Counter_Li)
Unique_List_Votes.append(Counter_0Tooley)
Total_Votes = sum(Unique_List_Votes)

#Make a dictionary to combine Candidate and their Total Votes

Percent_Khan = (Counter_Khan/Total_Votes)*100
Percent_Corey = (Counter_Correy/Total_Votes)*100
Percent_Li = (Counter_Li/Total_Votes)*100
Percent_0Tooley = (Counter_0Tooley/Total_Votes)*100

print(f"Total Votes: {Total_Votes}")
print("-----------------------------------")
print(f"Khan: {round(Percent_Khan,5)}% ({Counter_Khan})")
print(f"Correy: {round(Percent_Corey,5)}% ({Counter_Correy})")
print(f"Li: {round(Percent_Li,5)}% ({Counter_Li})")
print(f"O'Tooley: {round(Percent_0Tooley,3)}% ({Counter_0Tooley})")
print("-----------------------------------")
print("Winner: Khan")
print("-----------------------------------")


    
