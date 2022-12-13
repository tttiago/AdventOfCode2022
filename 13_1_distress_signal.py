import ast

with open("./data/input13.txt") as f:
    contents = f.read().split("\n\n")
    contents[-1] = contents[-1][:-1]


def compare(left, right):

    for left_val, right_val in zip(left, right):
        # Base case: compare two integers.
        if type(left_val) == int and type(right_val) == int:
            if left_val < right_val:
                return True
            elif left_val > right_val:
                return False
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
        return True
    elif len(left) > len(right):
        return False


index_sum = 0
for i, pairs in enumerate(contents):
    left, right = pairs.split("\n")
    # Convert strings to Python structures safely.
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)

    if compare(left, right):
        index_sum += i + 1

print(index_sum)
