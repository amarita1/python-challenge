import csv

totalmonths = []
Profit_Losses = []
Counter = 0

print("Financial Analysis")
print("-----------------------------")
with open("python-challenge/PyBank/Resources/budget_data.csv", 'r') as input_file:
     csvreader = csv.reader(input_file)
     header = next(csvreader)

     for row in csvreader:

          totalmonths.append(row[0])
          Profit_Losses.append(row[1])
          Profit_Losses = [int(i) for i in Profit_Losses]
          Changes = [Profit_Losses[i+1] - Profit_Losses[i] for i in range(len(Profit_Losses)-1)]
          Average = sum(Changes)/85

     print(f"Total Months : {len(totalmonths)} ")
     print(f"Total: ${sum(Profit_Losses)}")
     print(f"Average Change: ${round(Average, 2)}")
     
     Changes_Dc = {totalmonths[i + 1]: Changes[i] for i in range(len(Changes))}         
     Greatest_Increase = (max(Changes))
     Greatest_Decrease = (min(Changes))

     for month, changes in Changes_Dc.items():
          if changes == Greatest_Increase:
               print(f"Greatest Increase in Profits: {month} (${Greatest_Increase})")
          elif changes == Greatest_Decrease:
               print(f"Greatest Decrease in Profits: {month} (${Greatest_Decrease})")

     


     
     
          
     

     


       
         

        



         
         
      

        
            



     

     


    
    