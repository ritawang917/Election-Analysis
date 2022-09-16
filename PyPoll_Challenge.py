import csv
import os
Election_file = os.path.join ("Resources", "election_results.csv")
   # imports the data set
Written_file = os.path.join ("Analysis", "Election-Analysis.text")
   # creates a text file to write the analyzation
Votes = 0

## CANDIDATES

Candidate_name_list = []
Candidate_and_counter = {}
Winning_candidate = ""
Winning_number_of_votes = 0
Winning_vote_percentage = 0

## COUNTIES

Counties_name_list = []
Counties_and_counter = {}
Winning_county = ""
Winning_county_number_of_votes = 0
Winning_county_vote_percentage = 0

with open (Election_file) as Election_data:
   Reading_file = csv.reader(Election_data)
   Skip_header = next(Reading_file)
      # Skips the header from being analyzed

   # For loop to get votes of each candidate and county, and total votes
   for row in Reading_file:
      Votes += 1      
      Candidate_name = row [2]
      Counties_name = row [1]

      if Candidate_name not in Candidate_name_list:
         Candidate_name_list.append(Candidate_name)
         Candidate_and_counter[Candidate_name] = 0
      Candidate_and_counter[Candidate_name] += 1
       
      if Counties_name not in Counties_name_list:
         Counties_name_list.append(Counties_name)
         Counties_and_counter[Counties_name] = 0
      Counties_and_counter[Counties_name] += 1

with open(Written_file, "w") as Txt_file:
   print(f'Election Results \n------------------------- \nTotal Votes: {Votes:,.0f} \n-------------------------')
   print(f'County Votes:')

   Written_text = (f'Election Results \n------------------------- \nTotal Votes: {Votes:,.0f} \n-------------------------')
   Txt_file.write(Written_text)
   Txt_file.write("\nCounty Votes: \n")

   # For loop to list out the voting stats of each county
   for County_name in Counties_and_counter:
      Number_of_county_votes = Counties_and_counter[County_name]
      County_vote_percentage = (float(Number_of_county_votes) / float(Votes)) * 100

      print(f'{County_name}: {County_vote_percentage:.1f}% ({Number_of_county_votes:,.0f})')
      County_results = (f' \n{County_name}: {County_vote_percentage:.1f}% ({Number_of_county_votes:,.0f}) \n')
      Txt_file.write(County_results)

      # if statement to obtain the winning county
      if Number_of_county_votes > Winning_county_number_of_votes and County_vote_percentage > Winning_county_vote_percentage:
         Winning_county_number_of_votes = Number_of_county_votes
         Winning_county_vote_percentage = County_vote_percentage
         Winning_county = County_name
   
   print(f'-------------------------\n'
   f'Largest County Turnout: {Winning_county}\n'
   f'-------------------------')

   County_election_summary = (f'\n------------------------- \nLargest County Turnout: {Winning_county} \n-------------------------')
   Txt_file.write(County_election_summary)

   # For loop to list out the voting stats of each candidate
   for Candidate_name in Candidate_and_counter:
      Number_of_votes = Candidate_and_counter[Candidate_name]
      Vote_percentage = (float(Number_of_votes) / float(Votes)) * 100

      print(f'{Candidate_name}: {Vote_percentage:.1f}% ({Number_of_votes:,.0f})')
      Candidate_results = (f' \n{Candidate_name}: {Vote_percentage:.1f}% ({Number_of_votes:,.0f}) \n')
      Txt_file.write(Candidate_results)

      # if statement to obtain the winning candidate listed with its respective votes and vote percentage
      if Number_of_votes > Winning_number_of_votes and Vote_percentage > Winning_vote_percentage:
         Winning_number_of_votes = Number_of_votes
         Winning_vote_percentage = Vote_percentage
         Winning_candidate = Candidate_name

   print(f'------------------------- \nWinner: {Winning_candidate} \nWinning Vote Count: {Winning_number_of_votes:,.0f} \nWinning Percentage: {Winning_vote_percentage:.1f}% \n-------------------------') 
   Election_summary = (f'\n------------------------- \nWinner: {Winning_candidate} \nWinning Vote Count: {Winning_number_of_votes:,.0f} \nWinning Percentage: {Winning_vote_percentage:.1f}% \n-------------------------')
   Txt_file.write(Election_summary)