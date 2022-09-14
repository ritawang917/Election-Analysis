# Psuedocode
  # Total number of votes cast
  # A complete list of candidates who received votes
  # Total number of votes each candidate received
  # Percentage of votes each candidate won
  # The winner of the election based on popular vote
# import csv
# direct_file = "Resources/election_results.csv"
# election_results_data = open (direct_file, "r")
#     # "r" --> read the csv file
# # Analysis Performance on the csv file
# election_results_data.close()
# import csv
# direct_file = "Resources/election_results.csv"
# with open (direct_file) as election_results_data:
#     print(election_results_data)
import csv
import os
direct_file = os.path.join ("Resources", "election_results.csv")
   # imports the data set
written_file = os.path.join ("Analysis", "election_results.text")
   # creates a text file to write the analyzation
counter = 0
   # NOTE that this is located here because the counter needs to restart each time the file is opened
candidate_name_list = []
   # NOTE that this is located here because the list needs to restart each time the file is opened
candidate_and_counter = {}
   # NOTE that this is located here because the list needs to restart each time the file is opened
winning_candidate = ""
winning_number_of_votes = 0
winning_vote_percentage = 0
with open (direct_file) as data_set:
   # opens the data set that was originally imported in line 22
   read_file = csv.reader(data_set)
       # reads the csv file
   # iteration to print the row of the data set imported in line 22
   headers = next(read_file)
   # print (headers)
       # NOTE that this will print the FIRST line, because that is the next line
   # headers = next(data_set)
       # NOTE that this will print the SECOND line, because that is the next line after the first one
   for row in read_file:
       # NOTE that it is read_file because that is now the name of the file that is being read
       counter += 1
           #  NOTE that this is the same as counter = counter + 1
      
       candidate_name = row [2]
       if candidate_name not in candidate_name_list:
           candidate_name_list.append(candidate_name)
           candidate_and_counter[candidate_name] = 0
           # the names added are equal to zero --> print will result in 3 zeros corresponding to the associated name
       candidate_and_counter[candidate_name] += 1
           # NOTE that this has to be OUTSIDE the if-statement in order to add up the total
           # NOTE that the number of candidate name repeat = number of votes for the candidate
           # the total number of votes of EACH candidate
   print (f'{counter:,.0f}')
   print (candidate_name_list)
   print (candidate_and_counter)
with open(written_file, "w") as text_file:
   written_text = (f'Election Results \n------------------------- \nTotal Votes: {counter:,.0f} \n-------------------------')
   text_file.write(written_text)
   for candidate_name in candidate_and_counter:
      number_of_voters = candidate_and_counter[candidate_name]
      vote_percentage = (float(number_of_voters) / float(counter)) * 100
      candidate_results = (f' \n{candidate_name}: {vote_percentage:.1f}% ({number_of_voters:,.0f}) \n')
         # NOTE that the first \n returns the output in a new line such that it does not collide with the output in line 60
         # NOTE that the second \n returns the next iteration output in a new line
      text_file.write(candidate_results)
         # NOTE that this has to be in the for loop in order for the print to go through each candidate
      if number_of_voters > winning_number_of_votes and vote_percentage > winning_vote_percentage:
         winning_number_of_votes = number_of_voters
         winning_vote_percentage = vote_percentage
         winning_candidate = candidate_name
   election_summary = (f'\n------------------------- \nWinner: {winning_candidate} \nWinning Vote Count: {winning_number_of_votes:,.0f} \nWinning Percentage: {winning_vote_percentage:.1f}% \n-------------------------')
   text_file.write(election_summary)