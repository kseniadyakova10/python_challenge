import os
import csv
#create a path
csvpath = os.path.join("resources", "PyBank_budget_data.csv")

data = []
total_profit_loss = []
total_profit = 0
month_count = 0
greatest_inc = 0
greatest_dec = 0



#read the csv file
with open (csvpath) as csvfile:
    pybank = csv.reader(csvfile, delimiter=",")
    csv_header = next(pybank)
    for row in pybank:
        data.append(row)

# count total months in dataset
for row in data:
    month_count += 1

# count total profit of all months
for row in data:
   total_profit += int(row[1])

# define first row of data
previous_row = int(data[0][1])
data.pop(0)
# get monthly change total, from month to month
for row in data:
    month_to_month = int(row[1]) - previous_row
    previous_row = int(row[1])
    total_profit_loss.append(month_to_month)
    monthly_change = (sum(total_profit_loss) / len(total_profit_loss))

# get months for greates increase and decrease
for row in data:
     if int(row[1]) > greatest_inc:
        greatest_inc = int(row[1])
        greatest_inc_total = row[0], row[1]
     if int(row[1]) < greatest_dec:
        greatest_dec = int(row[1])
        greatest_dec_total = row[0], row[1]

# print all the results
print()
print("Financial Analysis:")
print("---------------------")
print("Total Months: " + str(month_count))
print("Total: " + str(total_profit))
print("Average Change: " + str(monthly_change))
print("Greatest Increase in Profits: " + str(greatest_inc_total))
print("Greatest Decrease in Profits: " + str(greatest_dec_total))

#write the txt file
output_path = os.path.join("..", "homework", "PyBank_revised.txt")

with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis:""\n")
    txtfile.write("---------------------""\n")
    txtfile.write("Total Months: " + str(month_count) + "\n")
    txtfile.write("Total: " + str(total_profit) + "\n")
    txtfile.write("Average Change: " + str(monthly_change) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(greatest_inc_total) + "\n")
    txtfile.write("Greatest Decrease in Profits: " + str(greatest_dec_total) + "\n")

    
