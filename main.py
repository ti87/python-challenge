import os
import csv

budgetdata_csv=os.path.join("..", "Resources", "budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")

months=[]
profit=[]
monthly_profit_change=[]

with open(budgetdata_csv) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")

    header = next(csv_reader)

    for row in csv_reader:
        months.append(row[0])
        profit.append(int(row[1]))

    for i in range(len(profit)-1):
        monthly_profit_change.append(profit[i+1]-profit[i])

max_increase=max(monthly_profit_change)
max_decrease=min(monthly_profit_change)

max_increase_month=monthly_profit_change.index(max(monthly_profit_change))+1
max_decrease_month=monthly_profit_change.index(min(monthly_profit_change))+1

output=(
"text"
"Financial Analysis"
"-----------------------------"
f'Total Months: {len(months)}'
f'Total: ${sum(profit)}'
f'Average Change: ${float(sum(profit)/len(profit)-1)}'
f'Greatest Increase in Profits: {months[max_increase_month]} (${str(max_increase)})'
f'Greatest Decrease in Profits: {months[max_decrease_month]} (${str(max_decrease)})'
)
print(output)


with open(pathout, "w") as txt_file:
    txt_file.write(output)



