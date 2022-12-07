# THIS IS DAY 7!

def part_one():
    parents = {}
    last_cd = ""
    sizes = {}
    with open("test_inputs.txt") as input_file:
        file = input_file.read().split('\n')
        for line in file: # for each line in file
            line = line.split()
            if (line[0] == "$"):
                if (line[1] == "cd"):
                    if (line[2] != ".."):
                        path = last_cd.split("!")
                        print(path)
                        path.append(line[2])
                        last_cd = "!".join(path)
                    else:
                        path = last_cd.split("!")
                        path.pop()
                        last_cd = "!".join(path)
            else:
                if (line[0] == "dir"):
                    parents[line[1]] = last_cd
                else:
                    if ("!".join(last_cd) in sizes):
                        sizes["!".join(last_cd)] += int(line[0])
                    else:
                        sizes["!".join(last_cd)] = int(line[0])

    print(sizes)

    result = 0
    for size in sizes:
        if sizes[size] <= 100000:
            result += sizes[size]

    print(f"Sum of part one {result}")
            
part_one()
