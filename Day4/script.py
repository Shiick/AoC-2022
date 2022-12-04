# THIS IS DAY 4!

self_contained = 0
overlapping = 0

already_counted = []

with open("inputs.txt") as input_file:
    file = input_file.read().split('\n\n')
    for line in file: # for each line in file
        line = line.split("\n")
        for sections in line:
            sections = sections.split(",")
            section_one, section_two = sections[0].split("-"), sections[1].split("-")
            set_a, set_b = range(int(section_one[0]), int(section_one[1]) + 1),range(int(section_two[0]), int(section_two[1]) + 1)
            if (set(set_a).issubset(set(set_b)) or set(set_b).issubset(set(set_a))):
                if (sections not in already_counted):
                    self_contained += 1
            if (any(i in set(set_a) for i in set(set_b))):
                overlapping += 1


print(f"Self contained part one: {self_contained}")
print(f"Overlapping part two: {overlapping}")