from functools import lru_cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=12)
inp = puzzle.input_data


def parse_row(row_str: str) -> tuple[str, tuple[int, ...]]:
    springs, tallies_str = row_str.split(" ")
    return springs, tuple(int(x) for x in tallies_str.split(","))


def tally_springs(springs_str: str) -> tuple[int, ...]:
    return tuple(
        len(spring_group)
        for spring_group in springs_str.split(".")
        if spring_group != ""
    )


@lru_cache
def count_possible_strings(
    template: str,
    template_index: int = 0,
    current_tally: tuple[int, ...] = (0,),
    *,
    aim: tuple[int, ...],
) -> int:
    # If we are at the end of the template
    if template_index == len(template):
        # If our current tally matches the aim, then we have found 1 way to match this aim, so we return 1
        #   (the + (0,) is to deal with the fact that we may end outside a group of damaged springs, we
        #    have a trailing 0)
        return 1 if (current_tally == aim or current_tally == (aim + (0,))) else 0

    # === Short circuiting logc ===
    # Cache tally length
    current_tally_len = len(current_tally)
    # Don't try short circuiting on the first element (prevent list out of bounds errors)
    if current_tally_len > 0:
        # Not being in a group of damaged springs is represented by the current tally ending in a 0
        #   the short circuiting logic functions differently depending on whether we are in a group
        #   of damaged springs or not
        if current_tally[-1] != 0:
            # If our current tally is too long, or the last item in the tally is larger than the aim,
            #   short circuit
            if (
                current_tally_len > len(aim)
                or current_tally[current_tally_len - 1] > aim[current_tally_len - 1]
            ):
                return 0
        # Only try to short circuit tallies ending in 0, if there is at least one element before it
        elif current_tally_len > 1:
            # If our tally is too long (taking into account the trailing 0)
            #   or the last item in the tally (ignoring the trailing 0) is larger than the aim
            #   short circuit
            if (
                current_tally_len > (len(aim) + 1)
                or current_tally[current_tally_len - 2] != aim[current_tally_len - 2]
            ):
                return 0

    # Determine what the options for the next character are
    if template[template_index] == "?":
        nexts = ["#", "."]
    else:
        nexts = [template[template_index]]
    # Go through each possible next character
    out = 0
    for next in nexts:
        # If the next character is a damaged spring, add 1 to the end of the current tally
        if next == "#":
            new_tally = current_tally[:-1] + (current_tally[-1] + 1,)
        # If the next character is a working spring, and the tallies don't currently end in
        #   a 0 (i.e. we are just leaving a group of damaged springs) add a 0, to mark that
        #   we are now out of that group
        elif current_tally[-1] != 0:
            new_tally = current_tally + (0,)
        # If the next character is a working spring, and we aren't in a group of damaged
        #   springs, the tally remains the same
        else:
            new_tally = current_tally

        # Get the total possible springs given this next character and add it to the
        #   output accumulator
        out += count_possible_strings(template, template_index + 1, new_tally, aim=aim)
    return out


def main():
    total_arrangemenets = 0
    for row in inp.splitlines():
        springs, desired_tallies = parse_row(row)
        arrs_this_row = count_possible_strings(
            "?".join([springs] * 5), aim=desired_tallies * 5
        )
        total_arrangemenets += arrs_this_row
    print(total_arrangemenets)


if __name__ == "__main__":
    main()
