with open("./data/input10.txt") as f:
    contents = f.read().splitlines()

register = 1
cycle = 0
signal_strengths = []


def update_signal_strengths(cycle, register, signal_strengths):
    if cycle in range(20, 221, 40):
        signal_strengths.append(register * cycle)


for command in contents:
    if command.startswith("noop"):
        cycle += 1
    elif command.startswith("addx"):
        cycle += 1
        update_signal_strengths(cycle, register, signal_strengths)
        register += int(command.split(" ")[-1])
        cycle += 1
    update_signal_strengths(cycle, register, signal_strengths)

print(sum(signal_strengths))
