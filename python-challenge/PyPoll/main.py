import os
import csv

#Setting the file path
poll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#open the file in read mode
with open (poll_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")

	#the code below ignores the header row. Don't use if you don't have a header row to begin with.
	csv_header = next(csv_file)

	print("  Election Results")
	print("--------------------")

	#Initialising counters and lists
	votes = []
	total = 0

	#total number of votes 
	#Looping through the rows, converting columns to lists. Creates a list of the ballot IDs from column A. 
	for row in csv_reader:
		votes.append(row[0]) #The 0 really means the first item in row 1 (base zero)
	#print(votes)

	total = len(votes)

	print("Total Votes: "+ str(total))
	print("--------------------")

#A complete list of candidates who received votes
#The total number of votes each candidate won

candidates=[]
numberwon = {}
votescast=0


#open the file in read mode
with open (poll_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	csv_header = next(csv_file)


	for row in csv_reader:
		votescast +=1
		candidates.append(row[2])

	
	candidatelist = set(candidates)


	totalCountPerPerson={}

	for people in candidatelist:
		totalCountPerPerson[people] = candidates.count(people)

	for people in candidatelist: 

#printout of candidates, percentage of votes won, and votes per candidate	
		print("{}: {:.3f}% ({})".format(people,totalCountPerPerson[people]/votescast *100,totalCountPerPerson[people]))

#Winner of election

max_value = max(totalCountPerPerson, key=totalCountPerPerson.get)
print("Winner: "+ str(max_value))

outputString = ""
for candidate in totalCountPerPerson.keys():
	candidateVoteCount = totalCountPerPerson[candidate]
	outputString = outputString + "\n" + candidate + ":"+  str(round( (candidateVoteCount/votescast)*100, 3)) + "% "  + "("+ str(candidateVoteCount) + ")"


output_path = os.path.join("analysis.txt")
with open(output_path, 'w') as textfile:
	
	election_results = (
		f"Election Results\n"
		f"----------------\n"

		f"Total Votes: {votescast}\n"
		f"------------------\n"

		#f"Candidates: {totalCountPerPerson}\n"
		f"Candidates: {outputString}\n"
		f"------------------\n"

		f"Winner: {max_value}\n")


	textfile.write(election_results)

	





