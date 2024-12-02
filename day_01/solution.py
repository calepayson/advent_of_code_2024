from collections import Counter

# Initialize the lists we'll be using
list_1 = []
list_2 = []

# Read the location_ids into their respective lists
with open("location_ids.txt", 'r') as file:
    for line in file:
        ids = line.strip().split()
        list_1.append(int(ids[0]))
        list_2.append(int(ids[1]))

# Sort each list of locations
list_1.sort()
list_2.sort()

# Find the total difference
total_difference = 0
for i in range(len(list_1)):
    difference = abs(list_1[i] - list_2[i])
    total_difference += difference

# Print the total difference of the two lists
print(f"Total difference: {total_difference}")

# Calculate the similarity score
# Converts each list into counter objects instead of iterating through each list
similarity_score = 0
counter_1 = Counter(list_1)
counter_2 = Counter(list_2)
for num in counter_1:
    if num in counter_2:
        similarity_score += num * counter_1[num] * counter_2[num]

# Print the similarity score of the two lists
print(f"Similarity score: {similarity_score}")
