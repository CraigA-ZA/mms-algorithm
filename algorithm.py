import sys

#Take array from command line argument
if len(sys.argv)  != 2:
    sys.exit("Usage: python algorithm.py <votes_array>")

votes = sys.argv[1].split(',')
counter = 0
candidate = None

for number in votes:
    if counter == 0:
        #Start counting a new candidate
        candidate = number
        counter = 1
    elif candidate == number:
        #Candidate for majority was hit again. Increment counter
        counter += 1
    else:
        #Hit a number that wasn't the current candidate. Decrement counter
        counter -= 1

#Confirm that the candidate is truly a majority
count_candidate = votes.count(candidate)
if count_candidate > len(votes) // 2:
    print(candidate)
else:
    print("No majority element")