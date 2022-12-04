with open("./data/input4.txt") as f:
    contents = f.read().splitlines()[:-1]

total_overlaps = 0
for line in contents:
    elf_1, elf_2 = line.split(",")
    elf_1_min, elf_1_max = [int(x) for x in elf_1.split("-")]
    elf_2_min, elf_2_max = [int(x) for x in elf_2.split("-")]

    # Ensure that elf1 is the one which starts in the lowest section.
    if elf_2_min < elf_1_min:
        elf_1_min, elf_1_max, elf_2_min, elf_2_max = elf_2_min, elf_2_max, elf_1_min, elf_1_max

    if elf_2_min <= elf_1_max:
        total_overlaps += 1

print(total_overlaps)
