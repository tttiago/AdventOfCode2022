with open("./data/input9.txt") as f:
    instructions = f.read().splitlines()

K_pos = {i: [0, 0] for i in range(10)}
visited = set()


def update_tail(head_pos, tail_pos):
    dif_x = head_pos[0] - tail_pos[0]
    dif_y = head_pos[1] - tail_pos[1]

    if abs(dif_x) <= 1 and abs(dif_y) <= 1:
        return

    if dif_x:
        tail_pos[0] += dif_x // abs(dif_x)
    if dif_y:
        tail_pos[1] += dif_y // abs(dif_y)


for instruction in instructions:
    direction, steps = instruction.split(" ")
    steps = int(steps)

    for step in range(steps):
        if direction == "U":
            K_pos[0][1] += 1
        elif direction == "D":
            K_pos[0][1] -= 1
        elif direction == "L":
            K_pos[0][0] -= 1
        elif direction == "R":
            K_pos[0][0] += 1

        for i in range(1, 10):
            update_tail(K_pos[i - 1], K_pos[i])

        visited.add(tuple(K_pos[9]))

print(len(visited))
