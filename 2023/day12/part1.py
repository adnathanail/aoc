from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=12)
inp = puzzle.input_data


def generate_all_possible_strings(template):
    if len(template) == 0:
        return [""]
    rests = generate_all_possible_strings(template[1:])
    if template[0] == "?":
        return ["#" + rest for rest in rests] + ["." + rest for rest in rests]
    else:
        return [template[0] + rest for rest in rests]


def tally_springs(springs_str):
    return [
        len(spring_group)
        for spring_group in springs_str.split(".")
        if spring_group != ""
    ]


assert tally_springs("##..##") == [2, 2]


def main():
    total_arrangemenets = 0
    for row in inp.splitlines():
        springs, tallies_str = row.split(" ")
        desired_tallies = [int(x) for x in tallies_str.split(",")]
        num_arrangements_this_row = 0
        for spring_str in generate_all_possible_strings(springs):
            if tally_springs(spring_str) == desired_tallies:
                num_arrangements_this_row += 1
        total_arrangemenets += num_arrangements_this_row
    print(total_arrangemenets)


if __name__ == "__main__":
    main()
