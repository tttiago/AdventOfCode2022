PRIORITIES = {ord("a") + i: i + 1 for i in range(26)}
PRIORITIES.update({ord("A") + i: i + 27 for i in range(26)})

with open("./data/input3.txt") as f:
    contents = f.read()

total_priority = 0
for line in contents.split("\n")[:-1]:
    part1, part2 = line[: len(line) // 2], line[len(line) // 2 :]
    repeated_item = None
    for item in part1:
        if item in part2:
            total_priority += PRIORITIES[ord(item)]
            break
print(total_priority)
