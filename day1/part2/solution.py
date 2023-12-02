with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

digits_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_first_digit(line):
    chars = ""
    for char in line:
        if not char.isnumeric():
            chars += char
        else:
            return int(char)
        for key in digits_dict:
            if key in chars:
                return digits_dict.get(key)


def get_last_digit(line):
    chars = ""
    for i in range(len(line), 0, -1):
        char = line[i-1]
        if not char.isnumeric():
            chars = char + chars
        else:
            return int(char)
        for key in digits_dict:
            if key in chars:
                return digits_dict.get(key)
            
sum = 0
for line in lines:
    sum += 10 * get_first_digit(line) + get_last_digit(line)

print(sum)