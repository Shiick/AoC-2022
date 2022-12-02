# THIS IS DAY 2

# THIS HAS TO BE THE WORST SOLUTION I'VE EVER CAME UP WITH. WILL BE REWORKED, HOPEFULLY.

def player_hand(player):
    return 1 if player == "X" else 2 if player == "Y" else 3  # 1 = X = rock, 2 = Y = paper, 3 = Z = scissors

def check_result_a(player): # ROCK
    return 3 if player == "X" else 6 if player == "Y" else 0 # 3 = X = rock = DRAW, 6 = Y = paper = WIN, 0 = Z = scissors = LOSS

def check_result_b(player): # PAPER
    return 3 if player == "Y" else 6 if player == "Z" else 0 # 3 = Y = paper = DRAW, 6 = Z = scissors = WIN, 0 = X = rock = LOSS

def check_result_c(player): # SCISSORS
    return 3 if player == "Z" else 6 if player == "X" else 0 # 3 = Z = scissors = DRAW, 6 = X = rock = WIN, 0 = Y = paper = LOSS

def check_result_a_part_two(player): # ROCK
    return 3 if player == "X" else 1 if player == "Y" else 2  # X = LOSS = scissors = 3, Y = DRAW = rock = 1, Z = WIN = paper = 2

def check_result_b_part_two(player): # PAPER
    return 1 if player == "X" else 2 if player == "Y" else 3  # X = LOSS = rock = 1, Y = DRAW = paper = 2, Z = WIN = scissors = 3

def check_result_c_part_two(player): # SCISSORS
    return 2 if player == "X" else 3 if player == "Y" else 1  # X = LOSS = paper = 2, Y = DRAW = scissors = 3, Z = WIN = rock = 1

def check_result_part_two(result):
    return 0 if result == "X" else 3 if result == "Y" else 6 # X = LOSS = 0, Y = DRAW = 3, Z = WIN = 6

total_points_part_one = 0
total_points_part_two = 0

with open("inputs.txt") as input_file:
    file = input_file.read().split('\n\n')
    for line in file: # for each line in file
        line = line.split("\n")
        for round in line:
            total_points_part_one += player_hand(round[2]) # get the amount of points depending on rock paper or scissors
            total_points_part_two += check_result_part_two(round[2]) #  get the amount of points depending on win loss or draw
            if (round[0] == "A"): # if enemy uses rock
                total_points_part_one += check_result_a(round[2]) # check if player win draw or loses
                total_points_part_two += check_result_a_part_two(round[2]) # check what the player should use
            if (round[0] == "B"): # if enemy uses paper
                total_points_part_one += check_result_b(round[2]) # check if player win draw or loses
                total_points_part_two += check_result_b_part_two(round[2]) # check what the player should use
            if (round[0] == "C"): # if enemy uses scissors
                total_points_part_one += check_result_c(round[2]) # check if player win draw or loses
                total_points_part_two += check_result_c_part_two(round[2]) # check what the player should use


print(f"Total points (p1): {total_points_part_one}")
print(f"Total points (p2): {total_points_part_two}")