import re

OUTCOMES = {"AB": "B", "AC": "A", "BC": "C"}
POINTS = {"A": 1, "B": 2, "C": 3}

with open("./data/input2.txt") as f:
    contents = f.read()

for pair in (("X", "A"), ("Y", "B"), ("Z", "C")):
    contents = re.sub(pair[0], pair[1], contents)

total_points = 0
for line in contents.split("\n")[:-1]:
    first_player, second_player = line[0], line[-1]
    total_points += POINTS[second_player]

    if first_player == second_player:
        total_points += 3

    elif OUTCOMES["".join(sorted(first_player + second_player))] == second_player:
        total_points += 6

print(total_points)
