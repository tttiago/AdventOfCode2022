import re


def find_stack_numbers_line(contents):
    for index, line in enumerate(contents):
        if "1" in line:
            return index


def find_number_of_stacks(contents, stack_numbers_line):
    return max([int(x) for x in contents[stack_numbers_line].split(" ") if x != ""])


def get_initial_stack_composition(contents, stack_numbers_line):
    initial_stack_lines = contents[:stack_numbers_line]
    initial_stacks = {i: [] for i in range(1, no_of_stacks + 1)}
    for line in initial_stack_lines[::-1]:
        for key in initial_stacks.keys():
            if (item := line[1 + 4 * (key - 1)]) != " ":
                initial_stacks[key].append(item)
    return initial_stacks


def get_operations(contents, stack_numbers_line):
    operation_lines = contents[stack_numbers_line + 2 :]
    operations = []
    for line in operation_lines:
        operations.append(tuple([int(x) for x in re.findall("[0-9]+", line)]))
    return operations


with open("./data/input5.txt") as f:
    contents = f.read().splitlines()

stack_numbers_line = find_stack_numbers_line(contents)
no_of_stacks = find_number_of_stacks(contents, stack_numbers_line)

stacks = get_initial_stack_composition(contents, stack_numbers_line)
operations = get_operations(contents, stack_numbers_line)

for n_items, init, final in operations:
    stacks[final].extend(stacks[init][-n_items:])
    del stacks[init][-n_items:]

print("".join([stacks[stack][-1] for stack in sorted(stacks) if stacks[stack]]))
