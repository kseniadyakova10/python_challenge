import os
import csv
#create a path
csvpath = os.path.join("resources", "election_data.csv")

data = []
voter_total = 0
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

#read the csv file
with open (csvpath) as csvfile:
    pypoll = csv.reader(csvfile, delimiter=",")
    csv_header = next(pypoll)
    for row in pypoll:
        data.append(row)

# count total votes in dataset
for row in data:
    voter_total += 1

# list candidates and number of votes
for row in data:
    if (row[2] == "Khan"):
        khan_total += 1
    elif (row[2] == "Correy"):
        correy_total += 1
    elif (row[2] == "Li"):
        li_total += 1
    else:
        otooley_total += 1

# percent of votes for each candidate
khan_percent = round((int(khan_total) / int(voter_total))*100, 2)
correy_percent = round((int(correy_total) / int(voter_total))*100, 2)
li_percent = round((int(li_total) / int(voter_total))*100, 2)
otooley_percent = round((int(otooley_total) / int(voter_total))*100, 2)

# winner based on max votes
winner = max(khan_total, correy_total, li_total, otooley_total)
if winner == khan_total:
    winner_name = "Khan"
elif winner == correy_total:
    winner_name = "Correy"
elif winnder == li_total:
    winner_name = "Li"
else:
    winner_name = "O'Tooley"

# print all the results
print()
print("Election Results:")
print("---------------------")
print("Total Voters: " + str(voter_total))
print("---------------------")
print("Khan: " + str(khan_percent) + "% " + str(khan_total))
print("Correy: " + str(correy_percent) + "% " + str(correy_total))
print("Li: " + str(li_percent) + "% " + str(li_total))
print("O'Tooley: " + str(otooley_percent) + "% " + str(otooley_total))
print("---------------------")
print("Winner:" + str(winner_name))
print("---------------------")

#write the txt file
output_path = os.path.join("..", "homework", "Pypoll_revised.txt")

with open(output_path, "w") as txtfile:
    txtfile.write("Election Results:""\n")
    txtfile.write("---------------------""\n")
    txtfile.write("Total Voters: " + str(voter_total) + "\n")
    txtfile.write("---------------------""\n")
    txtfile.write("Khan: " + str(khan_percent) + "% " + str(khan_total) + "\n")
    txtfile.write("Correy: " + str(correy_percent) + "% " + str(correy_total) + "\n")
    txtfile.write("Li: " + str(li_percent) + "% " + str(li_total) + "\n")
    txtfile.write("O'Tooley: " + str(otooley_percent) + "% " + str(otooley_total) + "\n")
    txtfile.write("---------------------""\n")
    txtfile.write("Winner:" + str(winner_name) + "\n")
    txtfile.write("---------------------""\n")