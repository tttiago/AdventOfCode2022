import re

OUTCOMES = {"AB": "B", "AC": "A", "BC": "C"}
REVERSED_OUTCOMES = {v: k for k, v in OUTCOMES.items()}
PLAY_POINTS = {"A": 1, "B": 2, "C": 3}
RESULT_POINTS = {"X": 0, "Y": 3, "Z": 6}

with open("./data/input2.txt") as f:
    contents = f.read()

total_points = 0
for line in contents.split("\n")[:-1]:
    first_player, result = line[0], line[-1]
    total_points += RESULT_POINTS[result]

    # Draw:
    if result == "Y":
        second_player = first_player
    # Lose:
    elif result == "X":
        for possible_game, winner in OUTCOMES.items():
            if first_player not in possible_game or winner != first_player:
                continue
            second_player = possible_game.replace(first_player, "")
    # Win:
    elif result == "Z":
        for possible_game, winner in OUTCOMES.items():
            if first_player not in possible_game or winner == first_player:
                continue
            second_player = winner

    total_points += PLAY_POINTS[second_player]

print(total_points)
