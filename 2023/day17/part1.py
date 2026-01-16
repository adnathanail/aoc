import heapq
import sys
from typing import Literal

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=17)
inp = puzzle.input_data

# inp = """241343231
# 321545353"""

inp = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

GRID = [[int(x) for x in row] for row in inp.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])


type Coord = tuple[int, int]


def coord_to_index(coord: Coord) -> int:
    return coord[0] + (coord[1] * GRID_WIDTH)


def index_to_coord(index: int) -> Coord:
    return (index % GRID_WIDTH, index // GRID_WIDTH)


def get_surrounding_squares(coord: Coord) -> list[tuple[Coord, str]]:
    out = []
    if coord[0] > 0:
        out.append(((coord[0] - 1, coord[1]), "<"))
    if coord[0] < (GRID_WIDTH - 1):
        out.append(((coord[0] + 1, coord[1]), ">"))
    if coord[1] > 0:
        out.append(((coord[0], coord[1] - 1), "^"))
    if coord[1] < (GRID_HEIGHT - 1):
        out.append(((coord[0], coord[1] + 1), "v"))
    return out


def get_valid_next_directions_from_path(path: str):
    if path == "":
        return ["^", ">", "v", "<"]
    out = []
    # We can always turn 90 degrees
    if path[-1] in ["<", ">"]:
        out += ["^", "v"]
    else:
        out += ["<", ">"]
    # If the last 3 instructions were the same, then we can't do that again
    if len(path) > 2 and path[-3] == path[-2] == path[-1]:
        return out
    # if not, then we can!
    out.append(path[-1])
    return out


# print(get_valid_next_directions_from_path(">>v>>"))


def adj(coord_index: int, current_path: str) -> list[tuple[int, int, str]]:
    coord = index_to_coord(coord_index)
    possible_next_directions = get_valid_next_directions_from_path(current_path)
    out = []
    for surr, dir_char in get_surrounding_squares(coord):
        if dir_char in possible_next_directions:
            out.append((coord_to_index(surr), GRID[surr[1]][surr[0]], dir_char))

    return out


def dijkstra(src_coord):
    src_index = coord_to_index(src_coord)

    paths_to_explore = []

    dist = [sys.maxsize for _ in range(GRID_WIDTH * GRID_HEIGHT)]
    path = [tuple() for _ in range(GRID_WIDTH * GRID_HEIGHT)]

    dist[src_index] = 0
    heapq.heappush(paths_to_explore, (0, src_index, ""))

    while paths_to_explore:
        current_path_distance, current_path_element, current_path = heapq.heappop(
            paths_to_explore
        )
        # print(current_path)

        # If this distance not the latest shortest one, skip it
        if current_path_distance > dist[current_path_element]:
            continue

        # Explore all neighbors of the current vertex
        for (
            next_path_element,
            current_to_next_distance,
            next_path_direction_char,
        ) in adj(current_path_element, current_path):
            # print(
            #     "\t",
            #     next_path_element,
            #     current_to_next_distance,
            #     next_path_direction_char,
            #     "\t",
            #     dist[current_path_element],
            #     dist[next_path_element],
            # )

            # If we found a shorter path to v through u, update it
            if (
                dist[current_path_element] + current_to_next_distance
                < dist[next_path_element]
            ):
                dist[next_path_element] = (
                    dist[current_path_element] + current_to_next_distance
                )
                path[next_path_element] = current_path + next_path_direction_char
                heapq.heappush(
                    paths_to_explore,
                    (
                        dist[next_path_element],
                        next_path_element,
                        current_path + next_path_direction_char,
                    ),
                )

    return dist, path


# def path_to_coords(path: str) -> list[Coord]:
#     curr = (0, 0)
#     out = []
#     for char in path:
#         if char == "<":
#             curr = (curr[0] - 1, curr[1])
#         elif char == ">":
#             curr = (curr[0] + 1, curr[1])
#         elif char == "^":
#             curr = (curr[0], curr[1] - 1)
#         elif char == "v":
#             curr = (curr[0], curr[1] + 1)
#         out.append(curr)
#     return out


dists, paths = dijkstra((0, 0))
print(dists)
print(paths)
# last_path_coords = path_to_coords(paths[-1])
# # for item in last_path_coords:
# #     print(item, last_path_coords.index(item), paths[-1][last_path_coords.index(item)])
# print(last_path_coords)
# for y in range(GRID_HEIGHT):
#     for x in range(GRID_WIDTH):
#         if (x, y) in last_path_coords:
#             print(paths[-1][last_path_coords.index((x, y))], end="")
#         else:
#             print(GRID[y][x], end="")
#     print()
