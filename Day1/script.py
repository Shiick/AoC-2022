elves = 0

inputs = []
current_input = 0

with open("inputs.txt") as input_file:
    for line in input_file:
        if (line.isspace()):
            inputs.append(current_input)
            current_input = 0
            elves += 1
        elif not line.endswith("\n"):
            value = int(line)
            current_input += value
            inputs.append(current_input)
            current_input = 0
            elves += 1
        else:
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