from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=12)
inp = puzzle.input_data


def generate_all_possible_strings(
    template,
    current_tally: tuple[int, ...] = tuple(),
    in_group=False,
    *,
    aim: tuple[int, ...],
):
    if len(template) == 0:
        return [""]
    if len(current_tally) > 0 and (
        len(current_tally) > len(aim)
        or current_tally[len(current_tally) - 1] > aim[len(current_tally) - 1]
    ):
        return []

    if template[0] == "?":
        firsts = ["#", "."]
    else:
        firsts = [template[0]]
    out = []
    for first in firsts:
        if first == "#":
            if in_group:
                new_tally = current_tally[:-1] + (current_tally[-1] + 1,)
            else:
                new_tally = current_tally + (1,)
            new_in_group = True
        else:
            new_tally = current_tally
            new_in_group = False

        out += [
            first + rest
            for rest in generate_all_possible_strings(
                template[1:], new_tally, new_in_group, aim=aim
            )
        ]
    return out


def tally_springs(springs_str: str) -> tuple[int, ...]:
    return tuple(
        len(spring_group)
        for spring_group in springs_str.split(".")
        if spring_group != ""
    )


def parse_row(row_str: str) -> tuple[str, tuple[int, ...]]:
    springs, tallies_str = row_str.split(" ")
    return springs, tuple(int(x) for x in tallies_str.split(","))


def count_valid_arrangements(springs: str, desired_tallies: tuple[int, ...]) -> int:
    num_arrangements_this_row = 0
    for spring_str in generate_all_possible_strings(springs, aim=desired_tallies):
        if tally_springs(spring_str) == desired_tallies:
            num_arrangements_this_row += 1
    return num_arrangements_this_row


def main():
    total_arrangemenets = 0
    for row in inp.splitlines():
        springs, desired_tallies = parse_row(row)
        total_arrangemenets += count_valid_arrangements(springs, desired_tallies)
        # total_arrangemenets += count_valid_arrangements("?".join([springs] * 5), desired_tallies * 5)
    print(total_arrangemenets)


if __name__ == "__main__":
    main()
