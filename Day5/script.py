# THIS IS DAY 5

import copy

grid = []

dictionary = {}
dictionary_p2 = {}
stacks = []

found_break = False

def part_one(line):
    instruction = line.split(" ")
    for i in range(int(instruction[1])): # for the instructed amount of crate
        dictionary[instruction[5]].append(dictionary[instruction[3]][len(dictionary[instruction[3]]) - 1]) # add the top crate on it's new stack
        del dictionary[instruction[3]][len(dictionary[instruction[3]]) - 1] # remove the crate from it's previous stack

def part_two(line):
    instruction = line.split(" ")
    for i in reversed(range(int(instruction[1]))): # for the instructed amount of crate, except the list is reversed to get the lowest one first and move up
        dictionary_p2[instruction[5]].append(dictionary_p2[instruction[3]][len(dictionary_p2[instruction[3]]) - (i+1)]) # get the crate from the top minus i + 1 (if no + 1, getting less crate than intended)
        del dictionary_p2[instruction[3]][len(dictionary_p2[instruction[3]]) - (i+1)] # remove the crate from it's previous stack

with open("inputs.txt") as input_file:
    file = input_file.read().split('\n')
    for line in file: # for each line in file
        if (found_break): # executing instructions here, after it mapped the grid
            instruction = line.split(" ")
            part_one(line)
            part_two(line)
            continue
        if(line == ""): # line 10 in inputs.txt (or line 5 in test_inputs)
            found_break = True
            stacks = ','.join(grid[len(grid)-1].split()).split(",")
            print(stacks)
            dictionary = dict.fromkeys(stacks, [])
            for stack in stacks:
                for row in range(len(grid) - 1):
                    if (grid[row][1+(int(stack)-1)*4] != " "):
                        dictionary[stack] = [grid[row][1+(int(stack)-1)*4]] + dictionary[stack]
            dictionary_p2 = copy.deepcopy(dictionary)
            continue
        grid.append(line)

print("Top crates part one: " + "".join([dictionary[dict][len(dictionary[dict]) - 1] for dict in dictionary]))
print("Top crates part two: " + "".join([dictionary_p2[dict][len(dictionary_p2[dict]) - 1] for dict in dictionary_p2]))