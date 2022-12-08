from typing import Optional


def check_tree_visibility(
        tree_height_grid: list[list[int]],
        coords: list[tuple[int, int]],
        include_same_height_trees: bool = False,
        max_tree_height: Optional[int] = None
) -> set[tuple[int, int]]:
    visible_trees = set()
    last_highest_tree_height = -1
    for coord in coords:
        i, j = coord
        if tree_height_grid[i][j] > last_highest_tree_height or (
                include_same_height_trees and tree_height_grid[i][j] == last_highest_tree_height):
            # if tree_height_grid[i][j] == last_highest_tree_height:
            #     print(1)
            visible_trees.add(coord)
            last_highest_tree_height = tree_height_grid[i][j]
        if max_tree_height is not None and tree_height_grid[i][j] >= max_tree_height:
            break
    return visible_trees
