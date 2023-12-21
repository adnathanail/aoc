from functools import cmp_to_key

from aocd.models import Puzzle
from utils import get_hand_type

puzzle = Puzzle(year=2023, day=7)

hands = []
for line in puzzle.input_data.split("\n"):
    line_split = line.split(" ")
    hands.append([line_split[0], int(line_split[1])])

card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}


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
