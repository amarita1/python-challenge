import csv

Original_List = []
Unqiue_List = []
Total_Votes = []

with open("python-challenge/PyPoll/Resources/election_data.csv", 'r') as input_file:
    csvreader = csv.reader(input_file)
    header = next(csvreader)

    for row in csvreader:
        Original_List.append(row[2])
        Total_Votes.append(row[0])
    print(Total_Votes)


    for x in Original_List:
        if x not in Unqiue_List:
            Unqiue_List.append(x)
        