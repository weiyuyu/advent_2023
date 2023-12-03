with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

def get_gear_positions(matrix):
    positions = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == "*":
                positions.append([x,y])
    return positions

def get_value(num):
    value = 0
    for i in range(len(num)):
        value += int(num[i]) * pow(10, len(num)-i-1)

    return value

def resolve_gear_ratio(nums):
    return get_value(nums[0]) * get_value(nums[1])

def get_gear_ratio_sum(matrix, gear_positions):
    sum = 0
    for gear_position in gear_positions:
        nums = []
        temp_num = []
        for x in range(max(0, gear_position[0]-1), min(len(matrix), gear_position[0]+2)):
            for y in range(0, len(matrix[x])):
                if x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[x]):
                    if matrix[x][y].isnumeric():
                        temp_num.append(matrix[x][y])
                    else:
                        if len(temp_num) > 0:
                            if abs(y-1-gear_position[1]) < 2 or abs(y-len(temp_num)-gear_position[1]) < 2:
                                nums.append(temp_num)
                            temp_num = []
            if len(temp_num) > 0:
                if abs(len(matrix[x])-len(temp_num)-gear_position[1]) < 2:
                    nums.append(temp_num)
                temp_num = []
        if len(nums) == 2:
            sum += resolve_gear_ratio(nums)
    return sum

matrix = []
for line in lines:
    row = []
    for char in line.rstrip():
        row.append(char)
    matrix.append(row)
gear_positions = get_gear_positions(matrix)
print(get_gear_ratio_sum(matrix, gear_positions))