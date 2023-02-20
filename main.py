import csv
import os


def header():
    print("\n")
    print("Financial Analysis")
    print("---------------------")

def currency(i):
    print('${:,.2f}'.format(i))
    
mnthcount = 0
total_amt = 0
ave_rate = 0

filepath = os.path.join('Resources','budget_data.csv')


with open (filepath, newline='', encoding='utf8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)  # skip the headers
    
    for lineread in csvreader:
        mnthcount = mnthcount + 1
        total_amt += float(lineread[1])
        if mnthcount == 1:
            recfirst = float(lineread[1])
        elif mnthcount != 1:
            reclast = float(lineread[1])
        
        # getting the highest and lowest profit
        if mnthcount == 1:
            temp_rec = lineread
            temp_amt = lineread[1]
        elif mnthcount != 1:
            lineread2 = lineread + temp_rec
            curr_date = lineread2[0]
            prev_date = lineread2[0]
            cur_profit = float(lineread[1]) - float(temp_amt)  # current computation of profit
            if mnthcount == 2:                
                previous_hprofit = cur_profit
                previous_lprofit = cur_profit
            elif mnthcount > 2:
                # assign the highest profit
                if cur_profit >= previous_hprofit:
                   highest_profit = cur_profit    
                   previous_hprofit = highest_profit
                if cur_profit < previous_hprofit:
                   highest_profit = previous_hprofit
                # assign the lowest profie
                if cur_profit <= previous_lprofit:
                   lowest_profit = cur_profit
                   previous_lprofit = lowest_profit
                if cur_profit > previous_lprofit:
                   lowest_profit = previous_lprofit

        temp_rec = lineread
        temp_amt = lineread[1]
            
ave_rate = float((recfirst-reclast)/(1-mnthcount))
high_profit = float(max(lineread[1]))
header()
print("Total Months: ", mnthcount)
print("Total : ", '${:.0f}'.format(total_amt))
print("Average Change: ", '${:,.2f}'.format(ave_rate))
print("Greatest Increase in Profits : ", '${:.0f}'.format(highest_profit))
print("Greatest Decrease in Profits : ", '${:.0f}'.format(lowest_profit))



# open file for output in text format
output_path = os.path.join('Resources', "financial.txt")
with open(output_path, 'w') as txtfile:
    
    txtfile.write(f"Financial Analysis " "\n")
    txtfile.write(f"---------------------" "\n")
    txtfile.write(f"Total Months: {mnthcount}" "\n")
    txtfile.write(f"Total : {'${:.0f}'.format(total_amt)}" "\n")
    txtfile.write(f"Average Change: {'${:,.2f}'.format(ave_rate)}" "\n")
    txtfile.write(f"Greatest Increase in Profits : {'${:.0f}'.format(highest_profit)}" "\n")
    txtfile.write(f"Greatest Decrease in Profits : {'${:.0f}'.format(lowest_profit)}" "\n")
