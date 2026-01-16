import heapq
import sys
from typing import Literal

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=17)
inp = puzzle.input_data
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


def get_surrounding_squares(coord: Coord) -> list[Coord]:
    out = []
    if coord[0] > 0:
        out.append((coord[0] - 1, coord[1]))
    if coord[0] < (GRID_WIDTH - 1):
        out.append((coord[0] + 1, coord[1]))
    if coord[1] > 0:
        out.append((coord[0], coord[1] - 1))
    if coord[1] < (GRID_HEIGHT - 1):
        out.append((coord[0], coord[1] + 1))
    return out


def adj(coord_index: int) -> list[tuple[int, int]]:
    coord = index_to_coord(coord_index)
    out = []
    for surr in get_surrounding_squares(coord):
        out.append((coord_to_index(surr), GRID[surr[1]][surr[0]]))

    return out


def dijkstra(src_coord):
    src_index = coord_to_index(src_coord)

    paths_to_explore = []

    dist = [sys.maxsize] * (GRID_WIDTH * GRID_HEIGHT)

    dist[src_index] = 0
    heapq.heappush(paths_to_explore, (0, src_index))

    while paths_to_explore:
        current_path_distance, current_path_element = heapq.heappop(paths_to_explore)

        # If this distance not the latest shortest one, skip it
        if current_path_distance > dist[current_path_element]:
            continue

        # Explore all neighbors of the current vertex
        for next_path_element, current_to_next_distance in adj(current_path_element):
            # If we found a shorter path to v through u, update it
            if (
                dist[current_path_element] + current_to_next_distance
                < dist[next_path_element]
            ):
                dist[next_path_element] = (
                    dist[current_path_element] + current_to_next_distance
                )
                heapq.heappush(
                    paths_to_explore, (dist[next_path_element], next_path_element)
                )
    return dist


print(dijkstra((0, 0)))
