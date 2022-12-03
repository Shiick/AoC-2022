# THIS IS DAY 3!

priority_part_one = 0
priority_part_two = 0

with open("inputs.txt") as input_file:
    file = input_file.read().split('\n\n')
    for line in file: # for each line in file
        line = line.split("\n")
        current_group_count = 0
        current_group_rucksacks = []
        for rucksack in line:
            first_compartment = rucksack[:len(rucksack)//2] # get first half of string
            second_compartment = rucksack[len(rucksack)//2:] # get second half of string
            common_type = list(set(first_compartment)&set(second_compartment))[0]
            priority_part_one += ord(common_type) - 96 if (common_type.islower()) else ord(common_type) - 38 # -96 for lowercase, -38 for uppercase. Based on Unicode 

            current_group_count += 1
            current_group_rucksacks.append(rucksack)
            if(current_group_count == 3):
                common_type = list(set(current_group_rucksacks[0])&set(current_group_rucksacks[1])&set(current_group_rucksacks[2]))[0]
                priority_part_two += ord(common_type) - 96 if (common_type.islower()) else ord(common_type) - 38 # -96 for lowercase, -38 for uppercase. Based on Unicode 
                current_group_count = 0
                current_group_rucksacks = []
                


print(f"Total priority for part one is {priority_part_one}")
print(f"Total priority for part two is {priority_part_two}")