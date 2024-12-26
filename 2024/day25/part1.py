from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=25)
input_data = puzzle.input_data


keys = []
locks = []
for k_or_l in input_data.split("\n\n"):
    kl_rows = k_or_l.split("\n")
    top_char = kl_rows[0][0]
    pin_0 = pin_1 = pin_2 = pin_3 = pin_4 = None
    for i in range(7):
        if pin_0 == None and kl_rows[i][0] != top_char:
            pin_0 = i
        if pin_1 == None and kl_rows[i][1] != top_char:
            pin_1 = i
        if pin_2 == None and kl_rows[i][2] != top_char:
            pin_2 = i
        if pin_3 == None and kl_rows[i][3] != top_char:
            pin_3 = i
        if pin_4 == None and kl_rows[i][4] != top_char:
            pin_4 = i
    if top_char == ".":
        keys.append((6 - pin_0, 6 - pin_1, 6 - pin_2, 6 - pin_3, 6 - pin_4))
    else:
        locks.append((pin_0 - 1, pin_1 - 1, pin_2 - 1, pin_3 - 1, pin_4 - 1))


def key_fits_lock(k, l):
    for i in range(5):
        if k[i] + l[i] > 5:
            return False
    return True


tot = 0
for key in keys:
    for lock in locks:
        if key_fits_lock(key, lock):
            tot += 1

print(tot)
