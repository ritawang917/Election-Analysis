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
direct_file = os.path.join("Resources", "election_results.csv")
    # imports the data set
written_file = os.path.join ("Analysis", "election_results.text")
    # creates a text file to write the analyzation
with open (direct_file) as data_set:
    # opens the data set that was originally imported in line 22
    read_file = csv.reader(data_set)
        # reads the csv file
    # iteration to print the row of the data set imported in line 22
    headers = next(data_set)
    print (headers)
        # NOTE that this will print the FIRST line, because that is the next line
    headers = next(data_set)
    print (headers)
        # NOTE that this will print the SECOND line, because that is the next line after the first one