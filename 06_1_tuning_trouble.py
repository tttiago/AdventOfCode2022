with open("./data/input6.txt") as f:
    contents = f.read()

marker_index = None
for index in range(3, len(contents)):
    if len(set(contents[index - 3 : index + 1])) == 4:
        marker_index = index + 1  # To correct for indexing starting at 1.
        break

print(marker_index)
