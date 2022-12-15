from collections import Counter, defaultdict

import numpy as np

SAND_START = (500, 0)

with open("./data/input14.txt") as f:
    contents = f.read().splitlines()

terrain_map = defaultdict(str)

for path in contents:
    points = path.split("->")
    points = [np.array(point.split(","), dtype=int) for point in points]

    for s_point, e_point in zip(points, points[1:]):
        dif = e_point - s_point
        dir = dif // max(abs(dif))
        while True:
            terrain_map[tuple(s_point)] = "#"
            if np.array_equal(s_point, e_point):
                break
            s_point += dir

max_y = max(terrain_map.keys(), key=lambda x: x[1])[1]
sand_out = False

while not sand_out:
    sand_x, sand_y = SAND_START
    while True:
        if not terrain_map[(sand_x, sand_y + 1)]:
            sand_y += 1
        elif not terrain_map[(sand_x - 1, sand_y + 1)]:
            sand_x -= 1
            sand_y += 1
        elif not terrain_map[(sand_x + 1, sand_y + 1)]:
            sand_x += 1
            sand_y += 1
        else:
            terrain_map[(sand_x, sand_y)] = "o"
            break

        if sand_y == max_y:
            sand_out = True
            break

print(Counter(terrain_map.values())["o"])
