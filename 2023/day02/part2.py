from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=2)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

game_power_sum = 0

for line in puzzle.input_data.splitlines():
    colon_split = line.split(": ")
    game_id = int(colon_split[0][5:])

    max_red = 0
    max_green = 0
    max_blue = 0

    for game in colon_split[1].split("; "):
        cube_numbers = game.split(", ")
        for cn in cube_numbers:
            if "red" in cn:
                max_red = max(max_red, int(cn.split(" ")[0]))
            if "green" in cn:
                max_green = max(max_green, int(cn.split(" ")[0]))
            if "blue" in cn:
                max_blue = max(max_blue, int(cn.split(" ")[0]))

    game_power_sum += max_red * max_green * max_blue

print(game_power_sum)
