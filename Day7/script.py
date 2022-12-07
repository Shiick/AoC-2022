# THIS IS DAY 7!

hierarchy = []
hierarchy.append("- / (dir)")

def find_all(current_increment):
    count = 0
    for item in hierarchy:
        if len(item) - len(item.lstrip()) == len(current_increment):
            count += 1
    return count

def part_one():
    current_folder = ""
    current_parents = []
    folders = {}
    children = {}
    with open("inputs.txt") as input_file:
        file = input_file.read().split('\n')
        for line in file: # for each line in file
            line = line.split()
            if (line[0] == "$"):
                if (line[1] == "cd"):
                    if (line[2] != ".."):
                        if (current_folder != ""):
                            children[current_folder] = children[current_folder] + [line[2]]
                            children[line[2]] = []
                        else:
                            children[line[2]] = []
                        current_folder = line[2]
                        current_parents.append(line[2])
                        folders[current_folder] = 0
                    else:
                        current_parents = current_parents[:-1]
                        current_folder = current_parents[-1]
            else:
                if (line[0] != "dir"):
                    folders[current_folder] += int(line[0])
    
    result = 0
    for child in children:
        folder_size = get_folder_size(child, children, folders)
        print(child, folder_size)
        if (folder_size <= 100000):
            result += folder_size
    print(f"Sum of part one {result}")

def get_folder_size(folder, children, folders):
    size = folders[folder]
    for child in children[folder]:
        folder_size = get_folder_size(child, children, folders)
        size += folder_size
    return size
            
part_one()
