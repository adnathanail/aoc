from functools import cmp_to_key

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=7)

hands = []
for line in puzzle.input_data.split("\n"):
    line_split = line.split(" ")
    hands.append([line_split[0], int(line_split[1])])

card_values = {"A": 14, "K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3,
               "2": 2, "J": 1}


def get_hand_type(hand):
    # Special case introduced by Jokers
    if hand == "JJJJJ":
        return 7

    char_tallies = {}
    num_js = 0
    for char in hand:
        if char == "J":
            num_js += 1
            continue
        char_tallies[char] = char_tallies.get(char, 0) + 1
    tally_nums = sorted(char_tallies.values())
    tally_nums[-1] += num_js

    if tally_nums == [5]:
        return 7
    elif tally_nums == [1, 4]:
        return 6
    elif tally_nums == [2, 3]:
        return 5
    elif tally_nums == [1, 1, 3]:
        return 4
    elif tally_nums == [1, 2, 2]:
        return 3
    elif tally_nums == [1, 1, 1, 2]:
        return 2
    return 1


def cust_cmp(x, y):
    x_hand_type = get_hand_type(x[0])
    y_hand_type = get_hand_type(y[0])
    if x_hand_type != y_hand_type:
        return x_hand_type - y_hand_type

    for i in range(5):
        if card_values[x[0][i]] != card_values[y[0][i]]:
            return card_values[x[0][i]] - card_values[y[0][i]]
    return 0


sorted_hands = sorted(hands, key=cmp_to_key(cust_cmp))

winnings = 0

for i in range(len(sorted_hands)):
    winnings += (i + 1) * sorted_hands[i][1]

print(winnings)
