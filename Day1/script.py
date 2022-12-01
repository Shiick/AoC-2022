# THIS IS DAY 1

elves = 0

inputs = []
current_input = 0

with open("inputs.txt") as input_file:
    for line in input_file: # for each line in file
        if (line.isspace()): # to check if the last elf is done
            inputs.append(current_input)
            current_input = 0
            elves += 1
        elif not line.endswith("\n"): # if last line in the file, add the last elf
            value = int(line)
            current_input += value
            inputs.append(current_input)
            current_input = 0
            elves += 1
        else: # random calorie value
            value = int(line)
            current_input += value

print(f"Total elves: {elves}")
first = max(inputs)
inputs.remove(first)
print(f"Most calories: {first}")
second = max(inputs)
inputs.remove(second)
print(f"Second most calories: {second}")
third = max(inputs)
inputs.remove(third)
print(f"Third most calories: {third}")

print(f"Total calories from top 3: {first+second+third}")