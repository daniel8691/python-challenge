#modules
import os 
import csv


def daniel(daniels_file):
    # Read in CSV file
    dates = []
    Profit_Losses = []
    with open(daniels_file) as csvfile:
        csvReader = csv.reader(csvfile,delimiter=',')
        csvheader = next(csvReader)
        for row in csvReader:
            dates.append(row[0])
            Profit_Losses.append(int(row[1]))



    print("Financial Analysis")
    print("---------------------------------------")

    #The total number of months included in the dataset
    print("Total Months: " + str(len(dates)))
    #The net total amount of "Profit/Losses" over the entire period
    print("Total: " + str(sum(Profit_Losses)))
    #The average of the changes in "Profit/Losses" over the entire period
    print("Average Change: $" + str((sum(Profit_Losses) / len(Profit_Losses))))

    #The greatest increase in profits (date and amount) over the entire period
    max_value = max(Profit_Losses)
    index_max = Profit_Losses.index(max_value)
    print("Greatest Increase in Profits: " + dates[index_max] + " ($"+ str(max_value) + ")")

    #The greatest decrease in losses (date and amount) over the entire period
    min_value = min(Profit_Losses)
    index_min = Profit_Losses.index(min_value)
    print("Greatest Decrease in Profits: " + dates[index_min] + " ($" + str(min_value) + ")")


daniel('budget_data.csv')