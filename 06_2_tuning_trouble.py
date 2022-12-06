with open("./data/input6.txt") as f:
    contents = f.read()

marker_index = None
for index in range(13, len(contents)):
    if len(set(contents[index - 13 : index + 1])) == 14:
        marker_index = index + 1  # To correct for indexing starting at 1.
        break

print(marker_index)
