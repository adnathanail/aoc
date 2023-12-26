from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=16)

grid = puzzle.input_data.split("\n")

visited = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
visited_deltas = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]

beams = [((0, 0), (0, 1))]

while beams:
    beam = beams.pop(0)
    loc, delta = beam

    print(loc)

    visited[loc[0]][loc[1]] = "#"
    if delta in visited_deltas[loc[0]][loc[1]]:
        continue
    visited_deltas[loc[0]][loc[1]].append(delta)

    next_loc = (loc[0] + delta[0], loc[1] + delta[1])
    while 0 <= next_loc[0] < len(grid) and 0 <= next_loc[1] < len(grid[0]):
        visited[next_loc[0]][next_loc[1]] = "#"
        if delta in visited_deltas[next_loc[0]][next_loc[1]]:
            break
        visited_deltas[next_loc[0]][next_loc[1]].append(delta)

        print("\t", next_loc)

        match grid[next_loc[0]][next_loc[1]]:
            case "|":
                if abs(delta[1]) == 1:
                    beams.append((next_loc, (-1, 0)))
                    beams.append((next_loc, (1, 0)))
                    break
            case "-":
                if abs(delta[0]) == 1:
                    beams.append((next_loc, (0, -1)))
                    beams.append((next_loc, (0, 1)))
                    break
            case "/":
                if delta[0] == 0:
                    beams.append((next_loc, (-delta[1], 0)))
                    break
                else:
                    beams.append((next_loc, (0, -delta[0])))
                    break
            case "\\":
                if delta[0] == 0:
                    beams.append((next_loc, (delta[1], 0)))
                    break
                else:
                    beams.append((next_loc, (0, delta[0])))
                    break

        # "." or "-"/"|" the wrong way
        visited[loc[0]][loc[1]] = "#"
        loc = next_loc
        next_loc = (loc[0] + delta[0], loc[1] + delta[1])

for row in visited:
    print("".join(row))

# print([char for x in visited for char in x].count("#"))