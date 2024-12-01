

# Initialize the lists we'll be using
list_1 = []
list_2 = []

# Read the location_ids into their respective lists
with open("location_ids.txt", 'r') as file:
    for line in file:
        ids = line.strip().split()
        list_1.append(ids[0])
        list_2.append(ids[1])

