from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=12)


def get_groups_from_line(lines):
    groups = []
    curr_group_size = 0
    for ch in line:
        if ch == "#":
            curr_group_size += 1
        elif curr_group_size > 0:
            groups.append(curr_group_size)
            curr_group_size = 0
    if curr_group_size > 0:
        groups.append(curr_group_size)
    return tuple(groups)


def string_replace(string, index, replacement):
    return string[:index] + replacement + string[index + 1 :]


def get_potential_arrangements(line, groups):
    # qs = [i for i in range(len(line)) if line[i] == "?"]
    groups = []
    curr_group_size = 0
    for ch in line:
        if ch == "#":
            curr_group_size += 1
        elif curr_group_size > 0:
            groups.append(curr_group_size)
            curr_group_size = 0
    if curr_group_size > 0:
        groups.append(curr_group_size)
    return tuple(groups)


inp = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

for line in inp.split("\n"):
    broken_line = line.split(" ")[0]
    known_groups = [int(i) for i in line.split(" ")[1].split(",")]
    print(broken_line, get_potential_arrangements(broken_line, known_groups))
    break
