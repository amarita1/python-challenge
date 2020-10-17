import csv

totalmonths = []
Profit_Losses = []

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

     print(max(Changes))
     print(min(Changes))
     


     
     
          
     

     


       
         

        



         
         
      

        
            



     

     


    
    