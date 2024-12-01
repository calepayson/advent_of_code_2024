

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

