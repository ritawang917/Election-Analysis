# Election-Analysis

## Project Overview
An employee from the Colorado Board of Elections gave the task to analyze an election audit of a recent local congressional election using Python programming language.

Task 1: Compute the total number of voters who voted
Task 2: Create a list of candidates who received votes
Task 3: Compute the total number of votes each candidate receives
Task 4: Compute the percentage of votes for each candidate
Task 5: Determine the winner of the election (the candidate with the most votes and percentage of vote; method: popular vote)

## Resources
- Data Source: election_results.csv
- Programming Tools: Python 3.6.1 and VS Code

## Election-Audit Results
    * A total of 369,711 votes were cast at the election
  - County Vote Breakdown
    * Jefferson: 38,855 votes
        * 10.5%
    * Denver: 306,055 votes
        * 82.8%
    * Arapahoe: 24,801 votes
        * 6.7%
        
![County Vote Breakdown](https://github.com/ritawang917/Election-Analysis/blob/main/County.png)

  From these results, we can see that Denver had the largest number of votes

  - Candidate Vote Breakdown
    * Charles Casper Stockham: 85,213 votes
        * 23.0%
    * Diana DeGette: 272,892 votes
        * 73.8%
    * Raymon Anthony Doane: 11,606 votes
        * 3.1%
        
![Candidate Vote Breakdown](https://github.com/ritawang917/Election-Analysis/blob/main/Candidate.png)

  From these results, we can see that Diana DeGette is the winning candidate with a total of 272,982 votes resulting in a vote percentage of 73.8%

## Summary of Analysis
  
  There were a total of 369,711 votes. Charles Casper Stockham had a vote percentage of 23.0% totaling to 85,213 supporters who voted for him, Diana DeGette had a vote percentage of 73.8% totaling to 272,892 votes, and Raymon Anthony Doane had a vote percentage of 3.1% totaling to 11,606 votes. From this comparison, it can be seen that the winner of the local congressional election is Diana Degette.

## Possible Election-Audit Script Alterations

  The script used to determine the winning candidate and county of a Colorado board of election can be used for other educational purposes. The script can be modified to see how many people from which country voted for a specific candidate; this analysis can then be used to determine if there is a correlation between the county the voters are from and the number of votes given to a respective candidate. This modification can be done by creating a nested for loop to count how many votes each candidate received from the respective counties. Additionally, the script can be used to see if there was a repeat in batch ID number by modifying the script to loop over each batch ID to make sure that there was no repeat to prevent any voter from voting more than once at the election. 
