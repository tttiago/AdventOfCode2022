with open("./data/input4.txt") as f:
    contents = f.read().splitlines()[:-1]

total_overlaps = 0
for line in contents:
    elf_1, elf_2 = line.split(",")
    elf_1_min, elf_1_max = [int(x) for x in elf_1.split("-")]
    elf_2_min, elf_2_max = [int(x) for x in elf_2.split("-")]

    if (
        elf_2_min <= elf_1_min <= elf_2_max
        or elf_2_min <= elf_1_max <= elf_2_max
        or (elf_2_min <= elf_1_min and elf_2_max >= elf_1_max)
    ):
        total_overlaps += 1
    elif (
        elf_1_min <= elf_2_min <= elf_1_max
        or elf_1_min <= elf_2_max <= elf_1_max
        or (elf_1_min <= elf_2_min and elf_1_max >= elf_2_max)
    ):
        total_overlaps += 1

print(total_overlaps)
