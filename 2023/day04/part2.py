from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=4)


def get_card_score(num_str):
    winning_num_str, got_num_str = num_str.split(" | ")
    winning_nums = {int(num) for num in winning_num_str.split(" ") if num != ""}
    got_nums = {int(num) for num in got_num_str.split(" ") if num != ""}
    return len(winning_nums.intersection(got_nums))


game_tallies = {}

for row in puzzle.input_data.splitlines():
    colon_split = row.split(":")
    game_id = int(colon_split[0][5:])

    if game_id not in game_tallies:
        game_tallies[game_id] = 0
    game_tallies[game_id] += 1

    for i in range(game_id + 1, game_id + 1 + get_card_score(colon_split[1])):
        if i not in game_tallies:
            game_tallies[i] = 0
        game_tallies[i] += game_tallies[game_id]

print(sum(game_tallies.values()))
