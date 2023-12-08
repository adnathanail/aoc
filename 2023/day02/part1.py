from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=2)

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

game_id_sum = 0

for line in puzzle.input_data.splitlines():
    colon_split = line.split(": ")
    game_id = int(colon_split[0][5:])

    game_is_possible = True

    for game in colon_split[1].split("; "):
        cube_numbers = game.split(", ")
        num_red = 0
        num_green = 0
        num_blue = 0
        for cn in cube_numbers:
            if "red" in cn:
                num_red = int(cn.split(" ")[0])
            if "green" in cn:
                num_green = int(cn.split(" ")[0])
            if "blue" in cn:
                num_blue = int(cn.split(" ")[0])
        if num_red > MAX_RED or num_green > MAX_GREEN or num_blue > MAX_BLUE:
            game_is_possible = False
            break
    if game_is_possible:
        game_id_sum += game_id

print(game_id_sum)
