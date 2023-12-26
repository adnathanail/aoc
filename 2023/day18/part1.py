from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=18)

x_max = 0
y_max = 0

loc = (0, 0)

grid = [["#"]]

inp = puzzle.examples[0].input_data
inp = puzzle.input_data


for row in inp.split("\n"):
    direc, num, col = row.split(" ")
    num = int(num)

    for i in range(num):
        match direc:
            case "R":
                loc = (loc[0], loc[1] + 1)
                if loc[1] > x_max:
                    x_max = loc[1]
                    for row in grid:
                        row.append(".")
            case "L":
                loc = (loc[0], loc[1] - 1)
                if loc[1] < 0:
                    x_max -= loc[1]
                    for row in grid:
                        row.insert(0, ".")
                    loc = (loc[0], loc[1] + 1)
            case "U":
                loc = (loc[0] - 1, loc[1])
                if loc[0] < 0:
                    y_max -= loc[0]
                    grid.insert(0, ["." for _ in range(len(grid[0]))])
                    loc = (loc[0] + 1, loc[1])
            case "D":
                loc = (loc[0] + 1, loc[1])
                if loc[0] > y_max:
                    y_max = loc[0]
                    grid.append(["." for _ in range(len(grid[0]))])
        grid[loc[0]][loc[1]] = "#"

inside_point = (40, 40)

grid[inside_point[0]][inside_point[1]] = "X"

# for row in grid:
#     print("".join(row))

# print()

points = [inside_point]
insides = set()
while points:
    point = points.pop(0)
    potential_points = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
    for pot in potential_points:
        if grid[pot[0]][pot[1]] in [".", "X"]:
            if pot not in insides:
                points.append(pot)
                insides.add(pot)

for inside in insides:
    grid[inside[0]][inside[1]] = "#"

# for row in grid:
#     print("".join(row))

print(sum([row.count("#") for row in grid]))
