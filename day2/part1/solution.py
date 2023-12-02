with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14
limit_dict = {
    "red": RED_LIMIT,
    "green": GREEN_LIMIT,
    "blue": BLUE_LIMIT
}

def is_game_content_valid(game_content_str):
    hands = game_content_str.rstrip().split("; ")
    for hand in hands:
        color_sets = hand.split(", ")
        for color_set in color_sets:
            set_content = color_set.split(" ")
            if int(set_content[0]) > limit_dict[set_content[1]]:
                return False

    return True        

sum = 0
for line in lines:
    game_num_str = line.split(": ")[0]
    game_num = int(game_num_str[5:])
    game_content_str = line.split(": ")[1]
    if is_game_content_valid(game_content_str):
        sum += game_num

print(sum)