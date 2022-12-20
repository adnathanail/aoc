from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)

abc_map = {"A": "R", "B": "P", "C": "S"}
xyz_map = {"X": "R", "Y": "P", "Z": "S"}
score_map = {"R": 1, "P": 2, "S": 3}


def p1_wins(p1, p2):
    return (
        (p2 == "R" and p1 == "P")
        or (p2 == "P" and p1 == "S")
        or (p2 == "S" and p1 == "R")
    )


def get_total_score(inp):
    total_score = 0
    for line in inp.split("\n"):
        they_play_coded, i_play_coded = line.split(" ")
        they_play, i_play = abc_map[they_play_coded], xyz_map[i_play_coded]
        total_score += score_map[i_play]
        if they_play == i_play:
            # draw
            total_score += 3
        elif p1_wins(i_play, they_play):
            # i win
            total_score += 6
    return total_score


print(
    get_total_score(
        """A Y
B X
C Z"""
    )
)
print(get_total_score(puzzle.input_data))
