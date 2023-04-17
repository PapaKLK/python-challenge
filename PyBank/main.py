###########################################
#  Author:  Kevin Krause
#  KU Data Analytics Bootcamp
#  Module 3 Challenge - Python Challenge
#           Budget Data
#  Due Date:  April 20, 2023
###########################################

# Get modules to allow reading and writing files and reading CSV files
import os
import csv

#budget data with be read and written to these paths
#the program main.py is running in folder PyBank and folders Reources 
#  and analysis are in the PyBank folder
bd_path = os.path.join('Resources', 'budget_data.csv')
bd_output = os.path.join('analysis','budget_report.txt')



# Open the csv file and move beyond the header row to
# the first row of actual data
with open(bd_path) as budget_file:

	budget_reader = csv.reader(budget_file, delimiter=',')
	budget_header = next(budget_reader)
    
# Initialize variable that will be used tracking totals,
# averages, and greatest increases and decreases.
	total_months = 0
	total_PL = 0
	prev_month_pl = 0
	total_pl_change = 0
	save_greatest_incrs = 0
	save_greatest_decrs = 0
	save_increase_month = ' '
	save_decrease_month = ' '
	pl_list = []

# Read each row of data after the header
	for row in budget_reader:
		budget_date = row[0]
		profit_or_loss = int(row[1])
		total_months += 1
		total_PL += profit_or_loss

# Determine if there was an increase or decrease from the
# Previous month's profit or loss and how much it was.
		if total_months > 1:
			pl_change = abs(save_pl - profit_or_loss)
			if save_pl > profit_or_loss:
				pl_change = pl_change * -1
			total_pl_change = total_pl_change + pl_change

# Determine what the greatest increase or decrease is
			if pl_change > 0:
				if pl_change > save_greatest_incrs:
					save_greatest_incrs = pl_change
					save_increase_month = budget_date
			else:
				if pl_change < save_greatest_decrs:
					save_greatest_decrs = pl_change
					save_decrease_month = budget_date

		save_pl = profit_or_loss

# End Reading File with


#################  Print and save summarization data. ###################################

tot_months = str(total_months)
tot_pl = str(total_PL)
avg_pl_change = round( ((total_pl_change) / (total_months - 1)  ),2)

# Save the summary report data so that it can be printed and saved to a text file
pl_list.append("Financial Analysis")
pl_list.append("----------------------------")
pl_list.append("Total Months:  " + str(total_months))
pl_list.append("Total:  $" + tot_pl)
pl_list.append("Average Change:  $" + str(avg_pl_change))
pl_list.append("Greatest Increase in Profits: " + save_increase_month + " ($" + str(save_greatest_incrs) +")")
pl_list.append("Greatest Decrease in Profits: " + save_decrease_month + " ($" + str(save_greatest_decrs) +")")


# Print the summary data to the terminal

for rptline in pl_list:
	print(rptline)


# Write the summary report data to a text file 
with open(bd_output,'w') as brpt:
	for rptline in pl_list:
		brpt.write(rptline)
		brpt.write('\n')

# End of script