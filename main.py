import csv
import os

# Initialize variables
numberMonths = 0
netProfit = 0
profitChange = []
greatestIncrease = {"date": "", "amount": 0}
greatestDecrease = {"date": "", "amount": 0}

# Read the CSV file and store data in a list
data = []
with open("budget_data.csv", newline="") as budgetDataCSV:
    reader = csv.reader(budgetDataCSV)
    header = next(reader)  # Skip the header row
    for row in reader:
        date, profit = row
        profit = int(profit)
        data.append({"date": date, "profit": profit})

# Calculate the total months and net profit
numberMonths = len(data)
netProfit = sum(item["profit"] for item in data)

# Calculate the profit changes and find greatest increase/decrease
for i in range(1, len(data)):
    change = data[i]["profit"] - data[i - 1]["profit"]
    profitChange.append(change)
    
    if change > greatestIncrease["amount"]:
        greatestIncrease["date"] = data[i]["date"]
        greatestIncrease["amount"] = change

    if change < greatestDecrease["amount"]:
        greatestDecrease["date"] = data[i]["date"]
        greatestDecrease["amount"] = change

# Calculate the average change
averageChange = sum(profitChange) / len(profitChange)

# Print the financial analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {numberMonths}")
print(f"Total: {netProfit}")
print(f"Average Change: {averageChange:.2f}")
print(f"Greatest Increase in Profits: {greatestIncrease['date']} ({greatestIncrease['amount']})")
print(f"Greatest Decrease in Profits: {greatestDecrease['date']} ({greatestDecrease['amount']})")

# Write results to a text file
output_path = os.path.join("analysis.txt")
with open(output_path, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------\n")
    textfile.write(f"Total Months: {numberMonths}\n")
    textfile.write(f"Total: {netProfit}\n")
    textfile.write(f"Average Change: {averageChange:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatestIncrease['date']} ({greatestIncrease['amount']})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatestDecrease['date']} ({greatestDecrease['amount']})\n")
