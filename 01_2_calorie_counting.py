with open("./data/input1.txt", "r") as f:
    raw_data = f.read().splitlines()

max_calories = [0, 0, 0]
cur_count = 0
for element in raw_data:
    if not element:
        if cur_count > max_calories[0]:
            max_calories.append(cur_count)
            max_calories.pop(0)
            max_calories.sort()
        cur_count = 0
        continue
    cur_count += int(element)

print(max_calories)
print(sum(max_calories))
