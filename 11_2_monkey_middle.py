import math
import re

with open("./data/input11.txt") as f:
    monkey_strings = f.read().split("\n\n")


def initialize_data(monkey_strings):
    """Transform the original monkey strings into a useful dictionary."""
    monkeys_dict = {}

    for monkey_string in monkey_strings:
        lines = monkey_string.split("\n")

        monkey_number = int(re.findall("[0-9]+", lines[0])[0])
        monkey_start_items = [int(x) for x in re.findall("[0-9]+", lines[1])]
        monkey_operation_str = lines[2].split("= ")[-1]
        monkey_divisor = int(re.findall("[0-9]+", lines[3])[0])
        monkey_destination_true = int(re.findall("[0-9]+", lines[4])[0])
        monkey_destination_false = int(re.findall("[0-9]+", lines[5])[0])

        monkeys_dict[monkey_number] = {
            "items": monkey_start_items,
            "operation": monkey_operation_str,
            "divisor": monkey_divisor,
            "destination": (monkey_destination_true, monkey_destination_false),
            "items_inspected": 0,
        }

    return monkeys_dict


def get_common_multiple(monkey_dict):
    divisors = [monkeys_dict[monkey]["divisor"] for monkey in monkeys_dict]
    return math.prod(divisors)


def compute_operation(operation_str, worry_level):
    """Compute the monkey operation given the operation string and the current worry_level."""
    operand_1, operation, operand_2 = operation_str.split(" ")
    operand_1 = worry_level if operand_1 == "old" else int(operand_1)
    operand_2 = worry_level if operand_2 == "old" else int(operand_2)
    if operation == "*":
        return operand_1 * operand_2
    elif operation == "+":
        return operand_1 + operand_2
    else:
        return NotImplementedError("Operator not defined.")


monkeys_dict = initialize_data(monkey_strings)
common_multuple = get_common_multiple(monkeys_dict)

for round in range(10_000):
    for monkey in monkeys_dict:
        cur_monkey_dict = monkeys_dict[monkey]
        n_items_to_remove = 0
        for item in cur_monkey_dict["items"]:
            cur_monkey_dict["items_inspected"] += 1
            worry_level = compute_operation(cur_monkey_dict["operation"], item)
            worry_level %= common_multuple
            if worry_level % cur_monkey_dict["divisor"] == 0:
                destination = cur_monkey_dict["destination"][0]
            else:
                destination = cur_monkey_dict["destination"][1]
            n_items_to_remove += 1
            monkeys_dict[destination]["items"].append(worry_level)
        # Remove items which where sent to other monkeys.
        for _ in range(n_items_to_remove):
            cur_monkey_dict["items"].pop(0)

total_inspected_items = [monkeys_dict[monkey]["items_inspected"] for monkey in monkeys_dict]
two_largest = sorted(total_inspected_items, reverse=True)[:2]
print(f"Monkey business level: {two_largest[0] * two_largest[1]}")
