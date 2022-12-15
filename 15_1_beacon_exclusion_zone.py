import re

WANTED_ROW = 2_000_000

no_beacon_locs = set()

with open("./data/input15.txt") as f:
    contents = f.read().splitlines()

for line in contents:
    sensor_x, sensor_y, beacon_x, beacon_y = [int(x) for x in re.findall("-?\d+", line)]
    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    if (sensor_y >= WANTED_ROW and (dif := sensor_y - WANTED_ROW) <= distance) or (
        sensor_y < WANTED_ROW and (dif := WANTED_ROW - sensor_y) <= distance
    ):
        remaining_steps = distance - dif
        for dx in range(-remaining_steps, remaining_steps + 1):
            no_beacon_locs.add(sensor_x + dx)
    if beacon_y == WANTED_ROW:
        no_beacon_locs.remove(beacon_x)

print(len(no_beacon_locs))
