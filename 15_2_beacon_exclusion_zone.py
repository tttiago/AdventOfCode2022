# Couldn't solve it myself.
# Idea from https://www.reddit.com/r/adventofcode/comments/zmcn64/comment/j0b90nr


import re

with open("./data/input15.txt") as f:
    contents = f.read().splitlines()

X_MULTIPLIER = 4_000_000
MAX_X = 4_000_000
MAX_Y = 4_000_000


def all_numbers(string):
    return [int(x) for x in re.findall("-?\d+", string)]


def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


data = [all_numbers(line) for line in contents]
radii = {
    (sensor_x, sensor_y): distance((sensor_x, sensor_y), (beacon_x, beacon_y))
    for sensor_x, sensor_y, beacon_x, beacon_y in data
}

sensors = radii.keys()

# y = x + a or y = -x + b
acoeffs, bcoeffs = set(), set()
for (sensor_x, sensor_y), radius in radii.items():
    acoeffs.add(sensor_y - sensor_x + radius + 1)
    acoeffs.add(sensor_y - sensor_x - radius - 1)
    bcoeffs.add(sensor_x + sensor_y + radius + 1)
    bcoeffs.add(sensor_x + sensor_y - radius - 1)

for a in acoeffs:
    for b in bcoeffs:
        intercept = ((b - a) // 2, (b + a) // 2)
        if 0 < intercept[0] < MAX_X and 0 < intercept[1] < MAX_Y:
            if all(distance(intercept, sensor) > radii[sensor] for sensor in sensors):
                print(X_MULTIPLIER * intercept[0] + intercept[1])
                break
