from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=16)

grid = puzzle.input_data.split("\n")


def get_energised_tiles(grid, initial):
    visited = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited_deltas = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    beams = [initial]

    while beams:
        beam = beams.pop(0)
        loc, delta = beam

        # print(loc)

        visited[loc[0]][loc[1]] = "#"
        if delta in visited_deltas[loc[0]][loc[1]]:
            continue
        visited_deltas[loc[0]][loc[1]].append(delta)

        while True:
            match grid[loc[0]][loc[1]]:
                case "|":
                    if abs(delta[1]) == 1:
                        beams.append((loc, (-1, 0)))
                        beams.append((loc, (1, 0)))
                        break
                case "-":
                    if abs(delta[0]) == 1:
                        beams.append((loc, (0, -1)))
                        beams.append((loc, (0, 1)))
                        break
                case "/":
                    if delta[0] == 0:
                        delta = (-delta[1], 0)
                    else:
                        delta = (0, -delta[0])
                case "\\":
                    if delta[0] == 0:
                        delta = (delta[1], 0)
                    else:
                        delta = (0, delta[0])

            loc = (loc[0] + delta[0], loc[1] + delta[1])

            # print("\t", loc)

            if not (0 <= loc[0] < len(grid) and 0 <= loc[1] < len(grid[0])):
                break

            visited[loc[0]][loc[1]] = "#"
            if delta in visited_deltas[loc[0]][loc[1]]:
                break

            visited_deltas[loc[0]][loc[1]].append(delta)

    # for row in visited:
    #     print("".join(row))

    return [char for x in visited for char in x].count("#")


energised_tiles = []

for i in range(len(grid)):
    from_left = ((i, 0), (0, 1))
    from_right = ((i, len(grid[0]) - 1), (0, -1))
    energised_tiles.append(get_energised_tiles(grid, from_left))
    energised_tiles.append(get_energised_tiles(grid, from_right))

for i in range(len(grid[0])):
    from_top = ((0, i), (1, 0))
    from_bottom = ((len(grid) - 1, i), (-1, 0))
    energised_tiles.append(get_energised_tiles(grid, from_top))
    energised_tiles.append(get_energised_tiles(grid, from_bottom))

print(max(energised_tiles))
