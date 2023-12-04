with open('files/input.txt', 'r') as input_file:
    lines = input_file.readlines()
input_file.close()

def process_matches(num_cards, idx, line):
    card_content = line.split(": ")[1]
    winning_nums = set(card_content.split(" | ")[0].split())
    nums = card_content.split(" | ")[1].split()
    matches = 0
    for num in nums:
        if num in winning_nums:
            matches += 1

    for i in range(matches):
        num_cards[idx+i+1] += num_cards[idx]
    return num_cards
    

num_cards = [1]*len(lines)
for i in range(len(lines)):
    num_cards = process_matches(num_cards, i, lines[i])
print(sum(num_cards))
    