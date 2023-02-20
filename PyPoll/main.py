import os
import csv
import numpy as np

poll_csv = os.path.join('Resources','election_data.csv')

Candidates = []

with open(poll_csv, newline = "") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  header = next(csvreader)

  for row in csvreader:
    Candidates.append(row[2])

Votes = np.array(np.unique(Candidates, return_counts=True))
Total =  len(Candidates)

Can1 = Votes[0,0]
Can2 = Votes[0,1]
Can3 = Votes[0,2]
Can4 = Votes[0,2]
Can1V = Votes[1,0]
Can2V = Votes[1,1]
Can3V = Votes[1,2]
Can4V = Votes[1,2]

PCan1V = float(Can1V) / float(Total) * 100
PCan2V = float(Can2V) / float(Total) * 100
PCan3V = float(Can3V) / float(Total) * 100
PCan4V = float(Can4V) / float(Total) * 100

winner = max(set(Candidates),key=Candidates.count)


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total))
print("-------------------------")
print(f"{Can1}  {round(PCan1V , 2)}%  ({Can1V})")
print(f"{Can2}  {round(PCan2V , 2)}%  ({Can2V})")
print(f"{Can3}  {round(PCan3V , 2)}%  ({Can3V})")
print(f"{Can4}  {round(PCan4V , 2)}%  ({Can4V})")
print("-------------------------")
print("Winner: " +  winner)
print("-------------------------")


text_file = open("PyPoll.txt","w",newline='')

text_file.write("Election Results\n")
text_file.write("-------------------------\n")
text_file.write("Total Votes: " + str(Total)  +"\n")
text_file.write("-------------------------\n")
text_file.write(f"{Can1}  {round(PCan1V , 2)}%  ({Can1V})\n")
text_file.write(f"{Can2}  {round(PCan2V , 2)}%  ({Can2V})\n")
text_file.write(f"{Can3}  {round(PCan3V , 2)}%  ({Can3V})\n")
text_file.write(f"{Can4}  {round(PCan4V , 2)}%  ({Can4V})\n")
text_file.write("-------------------------\n")
text_file.write("Winner: " +  winner + "\n")
text_file.write("-------------------------\n")
text_file.close()
