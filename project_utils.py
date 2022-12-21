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
