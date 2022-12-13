import ast
from functools import cmp_to_key

PACKETS_TO_ADD = [[[2]], [[6]]]

with open("./data/input13.txt") as f:
    contents = f.read().splitlines()


def compare(left, right):

    for left_val, right_val in zip(left, right):
        # Base case: compare two integers.
        if type(left_val) == int and type(right_val) == int:
            if left_val < right_val:
                return -1
            elif left_val > right_val:
                return 1
            # Go to the next value.
            continue

        # Cases where one of the values is not an int.
        elif not (type(left_val) == list and type(right_val) == list):
            if type(left_val) == int:
                left_val = [left_val]
            else:
                right_val = [right_val]

        # Return if a decision has been made. Keep searching if still unclear.
        if (res := compare(left_val, right_val)) != None:
            return res

    # Check cases where the comparison exhausted the pairs.
    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1


packets = [ast.literal_eval(packet) for packet in contents if packet]
packets.extend(PACKETS_TO_ADD)
packets.sort(key=cmp_to_key(compare))

index1 = packets.index(PACKETS_TO_ADD[0]) + 1
index2 = packets.index(PACKETS_TO_ADD[1]) + 1

print(index1 * index2)
