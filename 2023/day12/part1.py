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


def parse_row(row_str):
    springs, tallies_str = row_str.split(" ")
    return springs, [int(x) for x in tallies_str.split(",")]


def count_valid_arrangements(springs: str, desired_tallies: list[int]) -> int:
    num_arrangements_this_row = 0
    for spring_str in generate_all_possible_strings(springs):
        if tally_springs(spring_str) == desired_tallies:
            num_arrangements_this_row += 1
    return num_arrangements_this_row


def main():
    total_arrangemenets = 0
    for row in inp.splitlines():
        springs, desired_tallies = parse_row(row)
        total_arrangemenets += count_valid_arrangements(springs, desired_tallies)
    print(total_arrangemenets)


if __name__ == "__main__":
    main()
