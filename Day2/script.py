# THIS IS DAY ONE

results_part_one = {"A X": 4, # every result possible
                    "A Y": 8,
                    "A Z": 3,
                    "B X": 1,
                    "B Y": 5,
                    "B Z": 9,
                    "C X": 7,
                    "C Y": 2,
                    "C Z": 6}

results_part_two = {"A X": 3,
                    "A Y": 4,
                    "A Z": 8,
                    "B X": 1,
                    "B Y": 5,
                    "B Z": 9,
                    "C X": 2,
                    "C Y": 6,
                    "C Z": 7}

total_part_one = 0
total_part_two = 0

with open("inputs.txt") as input_file:
    file = input_file.read().split('\n\n')
    for line in file: # for each line in file
        line = line.split("\n")
        for round in line:
            total_part_one += results_part_one[round]
            total_part_two += results_part_two[round]

print(f"Result part one: {total_part_one}")
print(f"Result part two: {total_part_two}")