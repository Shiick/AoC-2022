# THIS IS DAY 6!

def part(line, packet_length):
    found = False
    offset = 0
    while not found:
        if (not all_different(line[offset + 0: offset + packet_length])):
            offset += 1
            continue
        found = True
    print(offset+packet_length)

def all_different(string):
    return len(set(string)) == len(string)

with open("inputs.txt") as input_file:
    file = input_file.read().split('\n')
    for line in file: # for each line in file
        part(line, 4)
        part(line, 14)