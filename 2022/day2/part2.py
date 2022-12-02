from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)

abc_map = {"A": "R", "B": "P", "C": "S"}
score_map = {"R": 1, "P": 2, "S": 3}
how_to_win_map = {"R": "P", "P": "S", "S": "R"}
how_to_lose_map = {"R": "S", "P": "R", "S": "P"}


def get_total_score(inp):
    total_score = 0
    for line in inp.split("\n"):
        they_play_coded, desired_outcome = line.split(" ")
        they_play = abc_map[they_play_coded]
        match desired_outcome:
            case "X":
                # lose
                i_play = how_to_lose_map[they_play]
            case "Y":
                # draw
                i_play = they_play
                total_score += 3
            case "Z":
                # win
                i_play = how_to_win_map[they_play]
                total_score += 6
            case _:
                raise Exception(f"Invalid desired outcome {desired_outcome}")
        total_score += score_map[i_play]
    return total_score


print(get_total_score(puzzle.input_data))
