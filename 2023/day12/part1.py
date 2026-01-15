from functools import lru_cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=12)
inp = puzzle.input_data
inp = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
# inp = "?????????#?# 1,1,7"


def tally_springs(springs_str: str) -> tuple[int, ...]:
    return tuple(
        len(spring_group)
        for spring_group in springs_str.split(".")
        if spring_group != ""
    )


def parse_row(row_str: str) -> tuple[str, tuple[int, ...]]:
    springs, tallies_str = row_str.split(" ")
    return springs, tuple(int(x) for x in tallies_str.split(","))


@lru_cache
def count_possible_strings(
    template: str,
    template_index: int = 0,
    current_tally: tuple[int, ...] = (0,),
    *,
    aim: tuple[int, ...],
) -> int:
    if template_index == len(template):
        return 1 if (current_tally == aim or current_tally == (aim + (0,))) else 0
    if (
        len(current_tally) > 0
        and (
            len(current_tally) > len(aim)
            or current_tally[len(current_tally) - 1] > aim[len(current_tally) - 1]
        )
        and current_tally[-1] != 0
    ):
        return 0

    if template[template_index] == "?":
        firsts = ["#", "."]
    else:
        firsts = [template[template_index]]
    out = 0
    for first in firsts:
        if first == "#":
            new_tally = current_tally[:-1] + (current_tally[-1] + 1,)
        elif current_tally[-1] != 0:
            new_tally = current_tally + (0,)
        else:
            new_tally = current_tally

        out += count_possible_strings(template, template_index + 1, new_tally, aim=aim)
    return out


def main():
    total_arrangemenets = 0
    for row in inp.splitlines():
        print(row)
        springs, desired_tallies = parse_row(row)
        # arrs_this_row = count_possible_strings(springs, aim=desired_tallies)
        arrs_this_row = count_possible_strings(
            "?".join([springs] * 5), aim=desired_tallies * 5
        )
        print(arrs_this_row)
        total_arrangemenets += arrs_this_row
        # break
    print(total_arrangemenets)


if __name__ == "__main__":
    main()
