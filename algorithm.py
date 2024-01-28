import sys

#Take array from command line argument
array = sys.argv[1].split(',')
counter = 0
candidate = None

for number in array:
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
count_candidate = array.count(candidate)
if count_candidate > len(array) // 2:
    print(candidate)
else:
    print("No majority element")