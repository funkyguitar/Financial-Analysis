import csv
import os
with open("Resources/budget_data.csv") as budgetDataCSV:
	bob = csv.reader(budgetDataCSV, delimiter=",")

# The total number of months included in the dataset - counts the number of rows minus the header row.  

	print("Financial Analysis")
	print("------------------")

	numberMonths = -1
	for dates,profit in bob:
		numberMonths+=1
	print("Total Months:",(numberMonths))
	
# The net total amount of "Profit/Losses" over the entire period - adds up the integers in column B in the spreadsheet 

with open("Resources/budget_data.csv") as budgetDataCSV:
	bob = csv.reader(budgetDataCSV, delimiter=",")
	header = next(bob)
	netProfit = 0
	for dates,profit in bob:
		netProfit+=int(profit)
	print("Total:",(netProfit))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

with open("Resources/budget_data.csv") as budgetDataCSV:
	bob = csv.reader(budgetDataCSV, delimiter=",")
	header = next(bob)

#The none value below indicates there's nothing to compare since it's #the beginning
	previousMonthProfit=None
#The line below creates a list, puts the monthly changes into a list. Variable that creates an empty list.
	profitChange=[]
	for dates,profit in bob:
#is not is actually Python syntax 
		if previousMonthProfit is not None:
			profitChange.append(int(profit) - previousMonthProfit)

		previousMonthProfit=int(profit)
	print("Average Change:",(sum(profitChange)/len(profitChange)))
	averageChange = sum(profitChange)/len(profitChange)

# The greatest increase in profits (date and amount) over the entire period


	budgetDataCSV.seek(0)
	header = next(bob)
	jim = max(profitChange)
	index = profitChange.index(jim)
	rowNumber=-1
	for gdates,profit in bob:
		if rowNumber==index:
			print("Greatest Increase in Profits:",gdates, jim)
		rowNumber+=1

# The greatest decrease in profits (date and amount) over the entire period

	budgetDataCSV.seek(0)
	header = next(bob)
	tom = min(profitChange)
	index = profitChange.index(tom)
	rowNumber=-1
	for idates,profit in bob:
		if rowNumber==index:
			print("Greatest Decrease in Profits:",idates, tom)
		rowNumber+=1


output_path = os.path.join("analysis.txt")
with open(output_path, 'w') as textfile:
	
	election_results = (
		f"Financial Analysis\n"
		f"------------------\n"

		f"Total Months:,{numberMonths}\n"

		f"Total:,{netProfit}\n"

		f"Average Change:,{averageChange}\n"

		f"Greatest Increase in Profits:,{gdates}, {jim}\n"

		f"Greatest Decrease in Profits:,{idates}, {tom}\n")


	textfile.write(election_results)

	


