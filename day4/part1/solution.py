with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

def get_line_points(line):
    card_content = line.split(": ")[1]
    winning_nums = set(card_content.split(" | ")[0].split())
    nums = card_content.split(" | ")[1].split()
    matches = 0
    for num in nums:
        if num in winning_nums:
            matches += 1
    if matches > 0:
        return pow(2, matches-1)
    return 0

points_sum = 0
for line in lines:
    points_sum += get_line_points(line.rstrip())
print(points_sum)
    