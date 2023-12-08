def get_hand_type(hand):
    char_tallies = {}
    for char in hand:
        char_tallies[char] = char_tallies.get(char, 0) + 1
    tally_nums = sorted(char_tallies.values())
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
