from collections import defaultdict

with open("./data/input7.txt") as f:
    contents = f.read().splitlines()


def create_size_dict(contents):
    folder_sizes = defaultdict(int)

    current_folder = []
    for line in contents:
        if line.startswith("$ cd"):
            folder_name = line.split(" ")[-1]
            if folder_name == "..":
                current_folder.pop()
                continue
            elif folder_name == "/":
                folder_name = ""
                current_folder = []
            current_folder.append(folder_name)
        elif not line.startswith("$") and not line.startswith("dir"):
            file_size = int(line.split(" ")[0])
            for depth in range(1, len(current_folder) + 1):
                folder_sizes["/".join(current_folder[:depth])] += file_size

    return folder_sizes


folder_sizes = create_size_dict(contents)

total_size = 0
for folder_size in folder_sizes.values():
    if folder_size <= 100000:
        total_size += folder_size

print(total_size)
