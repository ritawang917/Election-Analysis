counties = ["Arapahoe", "Denver", "Jefferson"]

if counties [1] == "Denver":
    print (counties [1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print ("Turn on the AC.")
else:
    print ("Open the windows.")
    
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

numbers = [0, 1, 2, 3, 4]

for num in numbers:
    print (num)

for num in range (5):
    print(num)

counties = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    # NOTE that the key word represents the county (Arapahoe, Denver, and Jefferson)
    # NOTE that the value word represents the voters (422829, 463353, 432438)

for county in counties:
    print(county)

for county in counties.keys():
    print(county)

for voters in counties.values():
    print(voters)

counties = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties.items():
    print(county, voters)

counties = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties.items():
    print(county + " county has " + str(voters) + " registered voters.")
        # NOTE that print can all print STRINGS so voters has to be changed from int to str

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for index in range(len(voting_data)):
    print(voting_data[index]["county"])
    print(voting_data[index]["registered_voters"])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                 {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:,.2f}% of the total votes.")

print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, registered_voters in counties_dict.items():
    print (f"{county} county has {registered_voters:,.0f} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for index in range (len (voting_data)):
        print (f' {voting_data[index]["county"]} county has {voting_data[index]["registered_voters"]:,.0f} registered voters.')

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

print(dir(int))
print(dir(float))
print(dir(bool))
print(dir(list))
print(dir(tuple))
print(dir(dict))
import datetime
print(dir(datetime))
import random
print(dir(random))
import pip
print(dir(pip))