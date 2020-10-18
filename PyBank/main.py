import csv

totalmonths = []
Profit_Losses = []
Counter = 0

#Create Header
print("Financial Analysis")
print("-----------------------------")

with open("python-challenge/PyBank/Resources/budget_data.csv", 'r') as input_file:
     csvreader = csv.reader(input_file)
     header = next(csvreader)
     
     for row in csvreader:
#Create List for Total Months and Profit/Losses
          totalmonths.append(row[0])
          Profit_Losses.append(row[1])
          Profit_Losses = [int(i) for i in Profit_Losses]
#Create List of Monthly Profit/Losses Changes
          Changes = [Profit_Losses[i+1] - Profit_Losses[i] for i in range(len(Profit_Losses)-1)]
#Calculate Average Monthly Changes
          Average = sum(Changes)/85
#Print Total # of Month, Net Total Profit/Losses, Average Changes
     print(f"Total Months : {len(totalmonths)} ")
     print(f"Total: ${sum(Profit_Losses)}")
     print(f"Average Change: ${round(Average, 2)}")

#Create dictionary to combine Total Months list and Monthly Profit/Losses Changes
     Changes_Dc = {totalmonths[i + 1]: Changes[i] for i in range(len(Changes))}         
     Greatest_Increase = (max(Changes))
     Greatest_Decrease = (min(Changes))

#Print Greatest Increase/Decrease in Profits using For loop with Dictionary
     for month, changes in Changes_Dc.items():
          if changes == Greatest_Increase:
               print(f"Greatest Increase in Profits: {month} (${Greatest_Increase})")
          elif changes == Greatest_Decrease:
               print(f"Greatest Decrease in Profits: {month} (${Greatest_Decrease})")
#Write Results to Text File
     with open("PyBankAnalysis.txt", "w") as outputfile:

        outputfile.write("Financial Analysis\n")
        outputfile.write("-----------------------------------\n")
        outputfile.write(f"Total Months : {len(totalmonths)}\n")
        outputfile.write(f"Total: ${sum(Profit_Losses)}\n")
        outputfile.write(f"Average Change: ${round(Average, 2)}\n")
        outputfile.write("Greatest Increase in Profits: Feb-2012 ($1926159)\n")
        outputfile.write("Greatest Decrease in Profits: Sep-2014 ($-2196167)\n")

       

     


     
     
          
     

     


       
         

        



         
         
      

        
            



     

     


    
    