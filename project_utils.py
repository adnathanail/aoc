def normalise_coord(coord: tuple[int, int], min_x: int, min_y: int) -> tuple[int, int]:
    return coord[0] - min_x, coord[1] - min_y


def get_from_grid(grid: list[list[str]], coord: tuple[int, int], min_x: int, min_y: int):
    norm_coord = normalise_coord(coord, min_x, min_y)
    return grid[norm_coord[1]][norm_coord[0]]


def set_on_grid(grid: list[list[str]], coord: tuple[int, int], value: str, min_x: int, min_y: int):
    norm_coord = normalise_coord(coord, min_x, min_y)
    grid[norm_coord[1]][norm_coord[0]] = value
