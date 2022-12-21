from numpy._typing import NDArray

Coord = tuple[int, int]

StrGrid = list[list[str]]
IntGrid = list[list[int]]


def normalise_coord(coord: Coord, min_x: int, min_y: int) -> Coord:
    return coord[0] - min_x, coord[1] - min_y


def get_from_grid(grid: StrGrid, coord: Coord, min_x: int, min_y: int):
    norm_coord = normalise_coord(coord, min_x, min_y)
    return grid[norm_coord[1]][norm_coord[0]]


def set_on_grid(grid: StrGrid, coord: Coord, value: str, min_x: int, min_y: int):
    norm_coord = normalise_coord(coord, min_x, min_y)
    grid[norm_coord[1]][norm_coord[0]] = value


def get_from_np_grid(grid: NDArray[int], coord: Coord, min_x: int, min_y: int):
    norm_coord = normalise_coord(coord, min_x, min_y)
    return grid[norm_coord[1]][norm_coord[0]]


def set_on_np_grid(grid: NDArray[int], coord: Coord, value: int, min_x: int, min_y: int):
    norm_coord = normalise_coord(coord, min_x, min_y)
    grid[norm_coord[1]][norm_coord[0]] = value


def manhattan_distance(p1: Coord, p2: Coord) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_min_max_x_y(coords: list[Coord]):
    min_x = max_x = coords[0][0]
    min_y = max_y = coords[0][1]

    for sb in coords:
        if sb[0] < min_x:
            min_x = sb[0]
        if sb[0] > max_x:
            max_x = sb[0]
        if sb[1] < min_y:
            min_y = sb[1]
        if sb[1] > max_y:
            max_y = sb[1]

    return min_x, max_x, min_y, max_y
