###########################################
#  Author:  Kevin Krause
#  KU Data Analytics Bootcamp
#  Module 3 Challenge - Python Challenge
#           Election Data
#  Due Date:  April 20, 2023
###########################################

# Get modules to allow reading and writing files and reading CSV files
import os
import csv

#Election data will be read and written to these paths
#the program main.py is running in folder PyBank and folders Reources 
#  and analysis are in the PyBank folder
elec_path = os.path.join('Resources', 'election_data.csv')
elec_output = os.path.join('analysis','election_report.txt')



# Open the csv file and move beyond the header row to
# the first row of actual data
with open(elec_path) as election_file:

	election_reader = csv.reader(election_file, delimiter=',')
	election_header = next(election_reader)

    
# Initialize variable that will be used tracking totals,
# averages, and greatest increases and decreases.
	total_votes = 0
	winner_count = 0
	candidate_list = []
	print_list = []
	print_list.append("Election Results")
	print_list.append("-------------------------")


# # Read each row of data after the header
	for row in election_reader:
 		Ballot_ID = row[0]
 		County = row[1]
 		Candidate = row[2]
 		candidate_list.append(Candidate)
 		total_votes += 1

print_list.append("Total Votes: " + str(total_votes))
print_list.append("-------------------------")
 

candidate_list.sort()
save_candidate = candidate_list[0]
vote_count = 0

for each_candidate in candidate_list:
	if each_candidate == save_candidate:
		vote_count += 1
	else:
		candidate_votes = str(vote_count)
		pct_votes = round(((vote_count/total_votes * 100)),3)
		prnt_pct_votes = str(pct_votes)
		if vote_count > winner_count:
			winner_count = vote_count
			winner_name = save_candidate

		print_list.append(save_candidate + ": " + prnt_pct_votes + "% (" + candidate_votes + ")")
		save_candidate = each_candidate
		vote_count = 1

# Need to pick up the last candidate since it won't fall thru to the else
if vote_count > winner_count:
	winner_count = vote_count
	winner_name = save_candidate

candidate_votes = str(vote_count)
pct_votes = round(((vote_count/total_votes * 100)),3)
prnt_pct_votes = str(pct_votes)
print_list.append(save_candidate + ": " + prnt_pct_votes + "% (" + candidate_votes + ")")
print_list.append("-------------------------")
print_list.append("Winner:  " + winner_name)


# # Print the summary data to the terminal

for rptline in print_list:
 	print(rptline)


# # Write the summary report data to a text file 
with open(elec_output,'w') as elecrpt:
 	for rptline in print_list:
 		elecrpt.write(rptline)
 		elecrpt.write('\n')

# End of script
