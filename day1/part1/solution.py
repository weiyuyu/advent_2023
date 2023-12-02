with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

nums = []
for line in lines:
    digits = []
    for char in line:
        if char.isnumeric():
            digits.append(int(char))
    num = 10*digits[0] + digits[-1]
    nums.append(num)

print(sum(nums))