import os
import csv

# Set File Path
csv_path = os.path.join('Resources', 'election_data.csv')
output_path = "Output.txt"
# Variables 
total_votes = 0
winner_count = 0
winner = ""
candidates = {}
candidates_percents = {}


# Read the File
with open(csv_path, newline = "") as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ",")
     header = next(csvreader)
     for row in csvreader:
        total_votes += 1
        #Find candidates and update votes
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        #  change to percent
        for k, v in candidates.items():
            candidates_percents[k] = round((v/total_votes) * 100, 3)

        # Find the winner  
        for k in candidates.keys():
            if candidates[k] > winner_count:
                winner = k
                winner_count = candidates[k]



# Print to terminal
print(f"Election Results")
print(f"-------------------------------------")
print(f"Total Votes:  {total_votes}")
print(f"-------------------------------------")
print(f"Khan: {candidates_percents['Khan']}% ({candidates['Khan']})")
print(f"Correy: {candidates_percents['Correy']}% ({candidates['Correy']})")
print(f"Li: {candidates_percents['Li']}% ({candidates['Li']})")
print(f"-------------------------------------")
print(f"Winner: {winner}")
print(f"-------------------------------------")

with open(output_path, 'w') as file:
    file.write(f"Election Results \n" )
    file.write(f"------------------------------------- \n") 
    file.write(f"Total Votes: {total_votes} \n")
    file.write(f"------------------------------------- \n")
    file.write(f"Khan: {candidates_percents['Khan']}% ({candidates['Khan']})\n")
    file.write(f"Correy: {candidates_percents['Correy']}% ({candidates['Correy']}) \n")
    file.write(f"Li: {candidates_percents['Li']}% ({candidates['Li']}) \n")
    file.write(f"------------------------------------- \n")
    file.write(f"Winner: {winner} \n")
    file.write(f"------------------------------------- \n")


   
   

