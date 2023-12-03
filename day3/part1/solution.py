with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

def get_nums(matrix):
    nums = []
    temp_nums = []
    positions = []
    for x in range(0, len(matrix)):
        position = []
        temp_num = []
        for y in range(0, len(matrix[x])):
            if matrix[x][y].isnumeric():
                if len(temp_num) < 1:
                    position.append(y)
                temp_num.append(matrix[x][y])
            else:
                if len(temp_num) > 0:
                    temp_nums.append(temp_num)
                    temp_num = []
                    position.append(y-1)
                    positions.append(position)
                    position = []
        if len(temp_num) > 0:
            temp_nums.append(temp_num)
            temp_num = []
            position.append(len(matrix[x])-1)
            positions.append(position)
            position = []
    
        for i in range(len(positions)):
            position = positions[i]
            valid = False
            for r in range(x-1, x+2):
                for c in range(position[0]-1, position[1]+2):
                    if r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r]):
                        if not matrix[r][c].isnumeric() and not matrix[r][c] == ".":
                            valid = True
            if valid:
                nums.append(temp_nums[i])
        temp_nums = []
        positions = []
    return nums

def get_sum_from_nums(nums):
    sum = 0
    for num in nums:
        for i in range(len(num)):
            sum += int(num[i]) * pow(10, len(num) - i -1)
    return sum


matrix = []
for line in lines:
    row = []
    for char in line.rstrip():
        row.append(char)
    matrix.append(row)

nums = get_nums(matrix)
print(get_sum_from_nums(nums))
