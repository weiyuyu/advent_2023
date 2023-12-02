with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

RED = "red"
BLUE = "blue"
GREEN = "green"

def get_power(game_content_str):
    cubes = {}
    hands = game_content_str.rstrip().split("; ")
    for hand in hands:
        color_sets = hand.split(", ")
        for color_set in color_sets:
            set_content = color_set.split(" ")
            if int(set_content[0]) > cubes.get(set_content[1], 0):
                cubes[set_content[1]] = int(set_content[0])
    
    return cubes.get(RED, 1) * cubes.get(BLUE, 1) * cubes.get(GREEN, 1)    

sum = 0
for line in lines:
    game_num_str = line.split(": ")[0]
    game_num = int(game_num_str[5:])
    game_content_str = line.split(": ")[1]
    sum += get_power(game_content_str)

print(sum)