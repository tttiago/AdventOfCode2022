PRIORITIES = {ord("a") + i: i + 1 for i in range(26)}
PRIORITIES.update({ord("A") + i: i + 27 for i in range(26)})

with open("./data/input3.txt") as f:
    contents = f.read()

total_priority = 0
for line1, line2, line3 in zip(*[iter(contents.split("\n")[:-1])] * 3):
    group_badge = None
    for item in line1:
        if item in line2 and item in line3:
            group_badge = item
            total_priority += PRIORITIES[ord(group_badge)]
            break
print(total_priority)
